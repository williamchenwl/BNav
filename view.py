from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, SubmitField
from wtforms.validators import DataRequired

class BQueryForm(FlaskForm):

    location = SelectMultipleField(u'当前位置: ', choices = [
        ('101', u'B101'),
        ('201', u'B201'),
        ('301', u'B301'),
        ('401', u'B401'),
        ('511', u'B511'),
    ])

    destination = SelectMultipleField(u'B楼目的地: ', choices = [
        ('101', u'B101'),
        ('201', u'B201'),
        ('301', u'B301'),
        ('401', u'B401'),
        ('511', u'B511'),
    ])
    
    submit = SubmitField(u'查询')

class QueryForm(FlaskForm):

    location = SelectMultipleField(u'当前位置: ', choices = [
        ('1', u'竹园1号楼'),
        ('2', u'竹园2号楼'),
        ('3', u'竹园3号楼'),
        ('4', u'竹园4号楼'),
        ('5', u'海棠5号楼'),
        ('6', u'海棠6号楼'),
        ('7', u'海棠7号楼'),
        ('8', u'海棠8号楼'),
        ('9', u'海棠9号楼'),
        ('10', u'海棠10号楼'),
        ('11', u'丁香11号楼'), 
        ('12', u'丁香12号楼'),
        ('13', u'丁香13号楼'),
        ('14',u'丁香14号楼'),
        ('15',u'丁香15号楼')
    ])

    destination = SelectMultipleField(u'B楼目的地: ', choices = [
        ('11', u'B210'), 
        ('12', u'B211'),
    ])
    
    submit = SubmitField(u'查询')


