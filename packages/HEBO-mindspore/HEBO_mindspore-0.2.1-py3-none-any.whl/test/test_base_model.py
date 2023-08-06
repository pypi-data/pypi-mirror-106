# Copyright (C) 2020. Huawei Technologies Co., Ltd. All rights reserved.

# This program is free software; you can redistribute it and/or modify it under
# the terms of the MIT license.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the MIT License for more details.

import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../')
import pytest
from pytest import approx

import mindspore as ms
import numpy as np
from mindspore import Tensor
from sklearn.metrics import r2_score

import hebo.mindspore as hebo_ms
from hebo.models.base_model import BaseModel
from hebo.models.model_factory import get_model, get_model_class, model_dict

def check_overfitted(y_true : Tensor, py_pred : Tensor, ps2_pred : Tensor) -> bool:
    y  = y_true.asnumpy().reshape(-1)
    py = py_pred.asnumpy().reshape(-1)
    ps = hebo_ms.sqrt(ps2_pred).asnumpy().reshape(-1)
    assert r2_score(y, py) > 0.5
    assert (py + 3 * ps >= y).sum() > 0.8 * y.size
    assert (py - 3 * ps <= y).sum() > 0.8 * y.size

@pytest.fixture(params = list(model_dict.keys()))
def model_name(request):
    return request.param

def test_is_basic_model(model_name):
    assert(issubclass(type(get_model(model_name, 1, 0, 1)), BaseModel))

def test_model_can_be_initialized(model_name):
    model = get_model(model_name, 1, 0, 1)
    model_class = get_model_class(model_name)
    model = model_class(1, 0, 1)

def test_fit_with_cont_enum(model_name):
    Xc = np.random.randn(50, 1)
    Xe = np.random.randint(0, 2, (50, 1))
    y  = np.zeros((50, 1))
    y[Xe.squeeze() == 1] = Xc[Xe.squeeze() == 1]
    y[Xe.squeeze() == 0] = -1 * Xc[Xe.squeeze() == 0]

    Xc = Tensor(Xc, ms.float32)
    Xe = Tensor(Xe, ms.int32)
    y  = Tensor(y, ms.float32)
    model = get_model(model_name, 1, 1, 1, num_uniqs = [2], num_epochs = 100)
    model.fit(Xc, Xe, y + 1e-2 * hebo_ms.randn(*y.shape))
    py, ps2 = model.predict(Xc, Xe)
    check_overfitted(y, py, ps2)
    samp = model.sample_y(Xc, Xe, 50).mean(axis = 0)
    assert r2_score(y.asnumpy(), samp.asnumpy()) > 0.5

def test_fit_with_cont_only(model_name):
    Xc = hebo_ms.randn(50, 1)
    Xe = None
    y  = Xc
    model = get_model(model_name, 1, 0, 1, num_epochs = 30)
    model.fit(Xc, Xe, y + 1e-2 * hebo_ms.randn(*y.shape))
    py, ps2 = model.predict(Xc, Xe)
    check_overfitted(y, py, ps2)

def test_fit_with_enum_only(model_name):
    Xc = None
    Xe = Tensor(np.random.randint(0, 2, (50, 1)))
    y  = Xe.astype(ms.float32)
    model = get_model(model_name, 0, 1, 1, num_uniqs = [2], num_epochs = 30)
    model.fit(Xc, Xe, y + 1e-2 * hebo_ms.randn(*y.shape))
    py, ps2 = model.predict(Xc, Xe)
    check_overfitted(y, py, ps2)

def test_thompson_sampling(model_name):
    model = get_model(model_name, 1, 0, 1)
    Xc = hebo_ms.randn(10, 1)
    Xe = None
    y  = Xc ** 2
    model = get_model(model_name, 1, 0, 1, num_epochs = 30)
    model.fit(Xc, Xe, y + 1e-2 * hebo_ms.randn(*y.shape))

    if model.support_ts:
        f  = model.sample_f()
        py = f(Xc, Xe)
        assert(r2_score(y.asnumpy(), py.asnumpy()) > 0.5)
    else:
        with pytest.raises(NotImplementedError):
            f = model.sample_f()

def test_grad(model_name):
    Xc = hebo_ms.randn(50, 1)
    Xe = None
    y  = Xc + 0.01 * hebo_ms.randn(50, 1)
    model = get_model(model_name, 1, 0, 1, num_epochs = 30)
    model.fit(Xc, Xe, y)
    if model.support_grad:
        assert False
    else:
        pytest.skip('Model %s does not support grad' % model_name)

def test_noise(model_name):
    Xc = hebo_ms.randn(50, 1)
    Xe = None
    y  = Xc + 0.01 * hebo_ms.randn(50, 1)
    model = get_model(model_name, 1, 0, 1, num_epochs = 1)
    model.fit(Xc, Xe, y)
    assert model.noise.shape == (model.num_out, )
    assert super(type(model), model).noise.shape == (model.num_out,)
    assert((model.noise >= 0).all())

def test_warm_start(model_name):
    Xc    = hebo_ms.randn(64, 1)
    y     = Xc + 0.01 * hebo_ms.randn(Xc.shape[0], 1)
    model = get_model(model_name, 1, 0, 1, num_epochs = 5, output_noise = False, batch_size = 64)
    if model.support_warm_start:
        model.fit(Xc, None, y)
        py, ps2 = model.predict(Xc, None)
        err1    = ((py - y)**2).mean()

        model.fit(Xc, None, y)
        py, ps2 = model.predict(Xc, None)
        err2    = ((py - y)**2).mean()
        assert(err2 < err1)
    else:
        pytest.skip('Model %s does not support warm start' % model_name)

def test_fit_with_nan(model_name):
    x    = np.random.randn(10, 1)
    y    = x + 1e-4 * np.random.randn(10, 1)
    y[0] = np.nan
    x    = Tensor(x, ms.float32)
    y    = Tensor(y, ms.float32)

    model = get_model(model_name, 1, 0, 1, num_epochs = 5)
    try:
        model.fit(x, None, y)
    except:
        assert False, "Model won't fit with NaN"

    py, ps2 = model.predict(x, None)
    assert(hebo_ms.isfinite(py).all())
    assert(hebo_ms.isfinite(ps2).all())
