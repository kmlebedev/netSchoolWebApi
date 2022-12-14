/*
 * NetSchool
 *
 * The API for the NetSchool irTech project
 *
 * API version: 5.10.63221
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package swagger

type DiaryAssignment struct {
	Mark *Mark `json:"mark,omitempty"`
	Attachments []Attachment `json:"attachments,omitempty"`
	Id int32 `json:"id,omitempty"`
	TypeId int32 `json:"typeId,omitempty"`
	AssignmentName string `json:"assignmentName,omitempty"`
	Weight int32 `json:"weight,omitempty"`
	DueDate string `json:"dueDate,omitempty"`
	ClassMeetingId int32 `json:"classMeetingId,omitempty"`
	ExistsTestPlan bool `json:"existsTestPlan,omitempty"`
}
