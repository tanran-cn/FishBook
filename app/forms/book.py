# _*_ coding: utf-8 _*_
from wtforms import Form, StringField, IntegerField
from wtforms.validators import length, NumberRange, DataRequired, Length, Regexp

__auther__ = "tanran"
__date__ = "2019/1/29 20:56"


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)


class DriftForm(Form):
    recipient_name = StringField(
        '收件人姓名', validators=[
            DataRequired(), Length(min=2, max=30, message='收件人姓名长度必须在2到20个字符之间'),
        ]
    )
    mobile = StringField('手机号', validators=[DataRequired(), Regexp('^1[0-9]{10}$', 0, '请输入争取的手机号')])
    message = StringField()
    address = StringField(validators=[DataRequired(), Length(min=10, max=70, message='地址还不到10个字吗？，请写详细一些')])
