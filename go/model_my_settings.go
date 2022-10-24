/*
 * NetSchool
 *
 * The API for the NetSchool irTech project
 *
 * API version: 5.10.63221
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package swagger

type MySettings struct {
	UserId int32 `json:"userId,omitempty"`
	FirstName string `json:"firstName,omitempty"`
	LastName string `json:"lastName,omitempty"`
	MiddleName string `json:"middleName,omitempty"`
	LoginName string `json:"loginName,omitempty"`
	BirthDate string `json:"birthDate,omitempty"`
	Roles []string `json:"roles,omitempty"`
	SchoolyearId int32 `json:"schoolyearId,omitempty"`
	WindowsAccount string `json:"windowsAccount,omitempty"`
	MobilePhone string `json:"mobilePhone,omitempty"`
	PreferedCom string `json:"preferedCom,omitempty"`
	Email string `json:"email,omitempty"`
	ExistsPhoto bool `json:"existsPhoto,omitempty"`
	UserSettings *MySettingsUserSettings `json:"userSettings,omitempty"`
}
