from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp, Length
from models import Edge, max_length


def lower(s):
    if s is not None:
        return s.lower()
    else:
        return s


def strip(s):
    if s is not None:
        return s.strip()
    else:
        return s


class EdgeForm(FlaskForm):
    l = StringField(
        "l",
        id="form_l",
        validators=[DataRequired(), Length(min=1, max=max_length)],
        filters=[lower, strip],
        render_kw={
            "placeholder": "friend 1",
            "style": "text-transform: lowercase;",
            "maxlength": max_length,
        },
    )
    r = StringField(
        "r",
        id="form_r",
        validators=[DataRequired(), Length(min=1, max=max_length)],
        filters=[lower, strip],
        render_kw={
            "placeholder": "friend 2",
            "style": "text-transform: lowercase;",
            "maxlength": max_length,
        },
    )
    how = StringField(
        "how",
        id="form_how",
        default="",
        validators=[Length(max=max_length)],
        filters=[lower, strip],
        render_kw={
            "placeholder": "school",
            "style": "text-transform: lowercase;",
            "maxlength": max_length,
        },
    )
    submit = SubmitField("make friends!")

    def validate(self, extra_validators=None):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        if self.l.data == self.r.data:
            return False

        if (
            Edge.query.filter_by(l=self.l.data, r=self.r.data).first()
            or Edge.query.filter_by(l=self.r.data, r=self.l.data).first()
        ):
            return False

        return True
