# io.swagger.client - Kotlin client library for NetSchool

## Requires

* Kotlin 1.4.30
* Gradle 5.3

## Build

First, create the gradle wrapper script:

```
gradle wrapper
```

Then, run:

```
./gradlew check assemble
```

This runs all tests and packages the library.

## Features/Implementation Notes

* Supports JSON inputs/outputs, File inputs, and Form inputs.
* Supports collection formats for query parameters: csv, tsv, ssv, pipes.
* Some Kotlin and Java types are fully qualified to avoid conflicts with types defined in Swagger definitions.
* Implementation of ApiClient is intended to reduce method counts, specifically to benefit Android targets.

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AssignmentApi* | [**assignmentTypes**](docs/AssignmentApi.md#assignmenttypes) | **GET** /grade/assignment/types | 
*DiaryApi* | [**diaryAssignnDetails**](docs/DiaryApi.md#diaryassignndetails) | **GET** /student/diary/assigns/{assignId} | 
*LoginApi* | [**getauthdata**](docs/LoginApi.md#getauthdata) | **POST** /auth/getdata | 
*LoginApi* | [**login**](docs/LoginApi.md#login) | **POST** /login | 
*LoginApi* | [**logindata**](docs/LoginApi.md#logindata) | **GET** /logindata | 
*LoginApi* | [**loginform**](docs/LoginApi.md#loginform) | **GET** /loginform | 
*LoginApi* | [**prepareemloginform**](docs/LoginApi.md#prepareemloginform) | **GET** /prepareemloginform | 
*LoginApi* | [**prepareloginform**](docs/LoginApi.md#prepareloginform) | **GET** /prepareloginform | 
*MysettingsApi* | [**mysettings**](docs/MysettingsApi.md#mysettings) | **GET** /mysettings | 
*MysettingsApi* | [**yearlist**](docs/MysettingsApi.md#yearlist) | **GET** /mysettings/yearlist | 
*StudentApi* | [**studentDiary**](docs/StudentApi.md#studentdiary) | **GET** /student/diary | 
*StudentApi* | [**studentDiaryInit**](docs/StudentApi.md#studentdiaryinit) | **GET** /student/diary/init | 

<a name="documentation-for-models"></a>
## Documentation for Models

 - [io.swagger.client.models.AssignmentTypes](docs/AssignmentTypes.md)
 - [io.swagger.client.models.AssignmentTypesInner](docs/AssignmentTypesInner.md)
 - [io.swagger.client.models.Attachment](docs/Attachment.md)
 - [io.swagger.client.models.Diary](docs/Diary.md)
 - [io.swagger.client.models.DiaryAssignDetails](docs/DiaryAssignDetails.md)
 - [io.swagger.client.models.DiaryAssignDetailsAttachments](docs/DiaryAssignDetailsAttachments.md)
 - [io.swagger.client.models.DiaryAssignDetailsSubjectGroup](docs/DiaryAssignDetailsSubjectGroup.md)
 - [io.swagger.client.models.DiaryAssignDetailsTeachers](docs/DiaryAssignDetailsTeachers.md)
 - [io.swagger.client.models.DiaryAssignment](docs/DiaryAssignment.md)
 - [io.swagger.client.models.DiaryLesson](docs/DiaryLesson.md)
 - [io.swagger.client.models.DiaryWeekDays](docs/DiaryWeekDays.md)
 - [io.swagger.client.models.GetAuthData](docs/GetAuthData.md)
 - [io.swagger.client.models.Login](docs/Login.md)
 - [io.swagger.client.models.LoginAccountInfo](docs/LoginAccountInfo.md)
 - [io.swagger.client.models.LoginAccountInfoCurrentOrganization](docs/LoginAccountInfoCurrentOrganization.md)
 - [io.swagger.client.models.LoginAccountInfoOrganizations](docs/LoginAccountInfoOrganizations.md)
 - [io.swagger.client.models.LoginAccountInfoUser](docs/LoginAccountInfoUser.md)
 - [io.swagger.client.models.LoginAccountInfoUserRoles](docs/LoginAccountInfoUserRoles.md)
 - [io.swagger.client.models.LoginAccountInfoUserRolesRole](docs/LoginAccountInfoUserRolesRole.md)
 - [io.swagger.client.models.LoginBody](docs/LoginBody.md)
 - [io.swagger.client.models.LoginData](docs/LoginData.md)
 - [io.swagger.client.models.LoginForm](docs/LoginForm.md)
 - [io.swagger.client.models.LoginRequestData](docs/LoginRequestData.md)
 - [io.swagger.client.models.Mark](docs/Mark.md)
 - [io.swagger.client.models.MySettings](docs/MySettings.md)
 - [io.swagger.client.models.MySettingsUserSettings](docs/MySettingsUserSettings.md)
 - [io.swagger.client.models.MySettingsYears](docs/MySettingsYears.md)
 - [io.swagger.client.models.MySettingsYearsInner](docs/MySettingsYearsInner.md)
 - [io.swagger.client.models.PrepareEmLoginForm](docs/PrepareEmLoginForm.md)
 - [io.swagger.client.models.PrepareEmLoginFormCountries](docs/PrepareEmLoginFormCountries.md)
 - [io.swagger.client.models.PrepareLoginForm](docs/PrepareLoginForm.md)
 - [io.swagger.client.models.StudentDiaryInit](docs/StudentDiaryInit.md)
 - [io.swagger.client.models.StudentDiaryInitStudents](docs/StudentDiaryInitStudents.md)

<a name="documentation-for-authorization"></a>
## Documentation for Authorization

<a name="bearerAuth"></a>
### bearerAuth


