# coding: utf-8

# flake8: noqa

"""
    NetSchool

    The API for the NetSchool irTech project  # noqa: E501

    OpenAPI spec version: 5.10.63221
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.assignment_api import AssignmentApi
from swagger_client.api.diary_api import DiaryApi
from swagger_client.api.login_api import LoginApi
from swagger_client.api.mysettings_api import MysettingsApi
from swagger_client.api.student_api import StudentApi
# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.assignment_types import AssignmentTypes
from swagger_client.models.assignment_types_inner import AssignmentTypesInner
from swagger_client.models.attachment import Attachment
from swagger_client.models.diary import Diary
from swagger_client.models.diary_assign_details import DiaryAssignDetails
from swagger_client.models.diary_assign_details_attachments import DiaryAssignDetailsAttachments
from swagger_client.models.diary_assign_details_subject_group import DiaryAssignDetailsSubjectGroup
from swagger_client.models.diary_assign_details_teachers import DiaryAssignDetailsTeachers
from swagger_client.models.diary_assignment import DiaryAssignment
from swagger_client.models.diary_lesson import DiaryLesson
from swagger_client.models.diary_week_days import DiaryWeekDays
from swagger_client.models.get_auth_data import GetAuthData
from swagger_client.models.login import Login
from swagger_client.models.login_account_info import LoginAccountInfo
from swagger_client.models.login_account_info_current_organization import LoginAccountInfoCurrentOrganization
from swagger_client.models.login_account_info_organizations import LoginAccountInfoOrganizations
from swagger_client.models.login_account_info_user import LoginAccountInfoUser
from swagger_client.models.login_account_info_user_roles import LoginAccountInfoUserRoles
from swagger_client.models.login_account_info_user_roles_role import LoginAccountInfoUserRolesRole
from swagger_client.models.login_body import LoginBody
from swagger_client.models.login_data import LoginData
from swagger_client.models.login_form import LoginForm
from swagger_client.models.login_request_data import LoginRequestData
from swagger_client.models.mark import Mark
from swagger_client.models.my_settings import MySettings
from swagger_client.models.my_settings_user_settings import MySettingsUserSettings
from swagger_client.models.my_settings_years import MySettingsYears
from swagger_client.models.my_settings_years_inner import MySettingsYearsInner
from swagger_client.models.prepare_em_login_form import PrepareEmLoginForm
from swagger_client.models.prepare_em_login_form_countries import PrepareEmLoginFormCountries
from swagger_client.models.prepare_login_form import PrepareLoginForm
from swagger_client.models.student_diary_init import StudentDiaryInit
from swagger_client.models.student_diary_init_students import StudentDiaryInitStudents
