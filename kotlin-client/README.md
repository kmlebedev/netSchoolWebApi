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

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/4.30.43656*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AssignmentApi* | [**assignmentTypes**](docs/AssignmentApi.md#assignmenttypes) | **GET** /grade/assignment/types | 
*DiaryApi* | [**diaryAssignnDetails**](docs/DiaryApi.md#diaryassignndetails) | **GET** /student/diary/assigns/{assignId} | 
*LoginApi* | [**logindata**](docs/LoginApi.md#logindata) | **GET** /logindata | 
*LoginApi* | [**prepareemloginform**](docs/LoginApi.md#prepareemloginform) | **GET** /prepareemloginform | 
*LoginApi* | [**prepareloginform**](docs/LoginApi.md#prepareloginform) | **GET** /prepareloginform | 
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
 - [io.swagger.client.models.DiaryAssignDetailsTeacher](docs/DiaryAssignDetailsTeacher.md)
 - [io.swagger.client.models.DiaryAssignment](docs/DiaryAssignment.md)
 - [io.swagger.client.models.DiaryLesson](docs/DiaryLesson.md)
 - [io.swagger.client.models.DiaryWeekDays](docs/DiaryWeekDays.md)
 - [io.swagger.client.models.LoginData](docs/LoginData.md)
 - [io.swagger.client.models.Mark](docs/Mark.md)
 - [io.swagger.client.models.PrepareEmLoginForm](docs/PrepareEmLoginForm.md)
 - [io.swagger.client.models.PrepareEmLoginFormCountries](docs/PrepareEmLoginFormCountries.md)
 - [io.swagger.client.models.PrepareLoginForm](docs/PrepareLoginForm.md)
 - [io.swagger.client.models.StudentDiaryInit](docs/StudentDiaryInit.md)
 - [io.swagger.client.models.StudentDiaryInitStudents](docs/StudentDiaryInitStudents.md)

<a name="documentation-for-authorization"></a>
## Documentation for Authorization

All endpoints do not require authorization.
