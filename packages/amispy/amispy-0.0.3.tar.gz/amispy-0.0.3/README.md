# pyamis

目的: 在`python`中生成`amis`的`json`配置  
解决问题:

1. 手写json配置太累了,配置复制粘贴重用性不好,减少手写json拼写出错概率
2. 可以在python中通过代码快速生成json配置
3. 要能和python的dict混用

### install
```
git clone https://github.com/1178615156/pyamis
pip install --editable .
```
### 示例

#### 生成Form组件

```python
# 首先import下
from pyamis.components import *

form = Form(
    target='target',
    mode="horizontal",
    # 可以看到属性能够直接插入dict
    controls=[
        {
            "type": "submit",
            "label": "登录"
        }
    ]
)
```

这样就生成了个Form配置了,然后转成json看看

```python
import json

json.dumps(form)
```

转成json

```json
{
  "type": "form",
  "mode": "horizontal",
  "controls": [
    {
      "type": "submit",
      "label": "\u767b\u5f55"
    }
  ],
  "target": "target"
}
```

#### 和dict进一步结合示例

```python
form_default_options = dict(
    title='条件',
    mode='horizontal',
    horizontal={
        "leftFixed": "sm"
    },
    submitOnInit=False,
    autoFocus=False,
)
form = Form(**form_default_options, #可以直接插入dict
            target='target')

# 直接设置属性也可以
form['controls'] = [
    {
        "type": "submit",
        "label": "提交"
    }
]
```

---


目前有的组件有:

- [Page](pyamis/components/page.py)
- [Chart](pyamis/components/chart.py)
- [Crud](pyamis/components/crud.py)
- [Action](pyamis/components/action.py)
- [Form](pyamis/components/form/form.py)
- 如果想用的组件不在上面的话可以直接写dict

### 快速启动示例

```python
from flask import Flask, send_file
from pyamis.components import *
import json

app = Flask("pyamis-test")


# app-pages配置
def site():
    return [
        # 第一个page
        AppPage(
            label='page-1',
            url='1',
            # 第一个page有2个子页
            children=[
                # 子页1
                AppPage(
                    label="page-1-1",
                    url='page-1-1',
                    schema_body=[
                        Form(controls=[
                            {
                                'type': 'text',
                                'name': "email",
                                'label': "email",
                                "required": True
                            },
                        ]),
                        "hello world 1 - 1"
                    ]
                ),
                # 子页2
                AppPage(
                    label="page-1-2",
                    url='page-1-2',
                    # schema_body=[...] 等价于
                    schema=Page(body=[
                        'hello page 1 - 2 '
                    ]),
                ),
            ]
        ),
        # 第二个page
        AppPage(
            label='page-2',
            url='2',
            #如果想用的组件没有的话,可以直接写json
            schema_body=[
                {
                    "type": "service",
                    "api": "https://3xsw4ap8wah59.cfc-execute.bj.baidubce.com/api/amis-mock/mock2/page/initData",
                    "body": {
                        "type": "panel",
                        "title": "$title",
                        "body": "现在是：${date}"
                    }
                }
            ],
        )
    ]

# print下生成的json配置
print(json.dumps(site(),indent=2))

@app.route('/')
def root():
    return send_file('test_index.html')


# 分页的json
@app.route("/pages/site.json")
def site_json():
    return {
        'data': {
            'pages': [
                dict(label='Home', url='/'),
                dict(children=site())
            ]
        }
    }


if __name__ == '__main__':
    app.run(port=8080, debug=True)

```