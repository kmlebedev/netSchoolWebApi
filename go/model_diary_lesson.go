/*
 * NetSchool
 *
 * The API for the NetSchool irTech project
 *
 * API version: 5.10.63221
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package swagger

type DiaryLesson struct {
	ClassmeetingId string            `json:"classmeetingId,omitempty"`
	Day            string            `json:"day,omitempty"`
	Number         int32             `json:"number,omitempty"`
	Room           string            `json:"room,omitempty"`
	StartTime      string            `json:"startTime,omitempty"`
	EndTime        string            `json:"endTime,omitempty"`
	SubjectName    string            `json:"subjectName,omitempty"`
	Assignments    []DiaryAssignment `json:"assignments,omitempty"`
}
