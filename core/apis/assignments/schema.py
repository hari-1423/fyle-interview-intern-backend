from marshmallow import Schema, EXCLUDE,ValidationsError, fields, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_enum import EnumField
from core.libs import assertions
from core.models.assignments import Assignment, GradeEnum
from core.libs.helpers import GeneralObject


class AssignmentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Assignment
        unknown = EXCLUDE

    id = auto_field(required=False, allow_none=True)
    content = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
    teacher_id = auto_field(dump_only=True)
    student_id = auto_field(dump_only=True)
    grade = auto_field(dump_only=True)
    state = auto_field(dump_only=True)

    @post_load
    def initiate_class(self, data_dict, many, partial):
        # pylint: disable=unused-argument,no-self-use
        assertions.assert_true(len(data_dict.keys()) > 0, 'No data was provided')
        return Assignment(**data_dict)


class AssignmentSubmitSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Integer(required=True, allow_none=False)
    teacher_id = fields.Integer(required=True, allow_none=False)

    @post_load
    def initiate_class(self, data_dict, many, partial):
        # pylint: disable=unused-argument,no-self-use
        return GeneralObject(**data_dict)


class AssignmentGradeSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Integer(required=True, allow_none=False)
    grade = EnumField(GradeEnum, required=True, allow_none=False)

    @post_load
    def initiate_class(self, data_dict, many, partial):
        # pylint: disable=unused-argument,no-self-use
        return GeneralObject(**data_dict)
