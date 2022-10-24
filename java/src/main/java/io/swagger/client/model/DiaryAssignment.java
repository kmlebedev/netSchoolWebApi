/*
 * NetSchool
 * The API for the NetSchool irTech project
 *
 * OpenAPI spec version: 5.10.63221
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.client.model.Attachment;
import io.swagger.client.model.Mark;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.threeten.bp.LocalDate;
/**
 * DiaryAssignment
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2022-10-24T12:37:15.210Z[GMT]")
public class DiaryAssignment {
  @SerializedName("mark")
  private Mark mark = null;

  @SerializedName("attachments")
  private List<Attachment> attachments = null;

  @SerializedName("id")
  private Integer id = null;

  @SerializedName("typeId")
  private Integer typeId = null;

  @SerializedName("assignmentName")
  private String assignmentName = null;

  @SerializedName("weight")
  private Integer weight = null;

  @SerializedName("dueDate")
  private LocalDate dueDate = null;

  @SerializedName("classMeetingId")
  private Integer classMeetingId = null;

  @SerializedName("existsTestPlan")
  private Boolean existsTestPlan = null;

  public DiaryAssignment mark(Mark mark) {
    this.mark = mark;
    return this;
  }

   /**
   * Get mark
   * @return mark
  **/
  @Schema(description = "")
  public Mark getMark() {
    return mark;
  }

  public void setMark(Mark mark) {
    this.mark = mark;
  }

  public DiaryAssignment attachments(List<Attachment> attachments) {
    this.attachments = attachments;
    return this;
  }

  public DiaryAssignment addAttachmentsItem(Attachment attachmentsItem) {
    if (this.attachments == null) {
      this.attachments = new ArrayList<Attachment>();
    }
    this.attachments.add(attachmentsItem);
    return this;
  }

   /**
   * Get attachments
   * @return attachments
  **/
  @Schema(description = "")
  public List<Attachment> getAttachments() {
    return attachments;
  }

  public void setAttachments(List<Attachment> attachments) {
    this.attachments = attachments;
  }

  public DiaryAssignment id(Integer id) {
    this.id = id;
    return this;
  }

   /**
   * Get id
   * @return id
  **/
  @Schema(description = "")
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }

  public DiaryAssignment typeId(Integer typeId) {
    this.typeId = typeId;
    return this;
  }

   /**
   * Get typeId
   * @return typeId
  **/
  @Schema(description = "")
  public Integer getTypeId() {
    return typeId;
  }

  public void setTypeId(Integer typeId) {
    this.typeId = typeId;
  }

  public DiaryAssignment assignmentName(String assignmentName) {
    this.assignmentName = assignmentName;
    return this;
  }

   /**
   * Get assignmentName
   * @return assignmentName
  **/
  @Schema(description = "")
  public String getAssignmentName() {
    return assignmentName;
  }

  public void setAssignmentName(String assignmentName) {
    this.assignmentName = assignmentName;
  }

  public DiaryAssignment weight(Integer weight) {
    this.weight = weight;
    return this;
  }

   /**
   * Get weight
   * @return weight
  **/
  @Schema(description = "")
  public Integer getWeight() {
    return weight;
  }

  public void setWeight(Integer weight) {
    this.weight = weight;
  }

  public DiaryAssignment dueDate(LocalDate dueDate) {
    this.dueDate = dueDate;
    return this;
  }

   /**
   * Get dueDate
   * @return dueDate
  **/
  @Schema(description = "")
  public LocalDate getDueDate() {
    return dueDate;
  }

  public void setDueDate(LocalDate dueDate) {
    this.dueDate = dueDate;
  }

  public DiaryAssignment classMeetingId(Integer classMeetingId) {
    this.classMeetingId = classMeetingId;
    return this;
  }

   /**
   * Get classMeetingId
   * @return classMeetingId
  **/
  @Schema(description = "")
  public Integer getClassMeetingId() {
    return classMeetingId;
  }

  public void setClassMeetingId(Integer classMeetingId) {
    this.classMeetingId = classMeetingId;
  }

  public DiaryAssignment existsTestPlan(Boolean existsTestPlan) {
    this.existsTestPlan = existsTestPlan;
    return this;
  }

   /**
   * Get existsTestPlan
   * @return existsTestPlan
  **/
  @Schema(description = "")
  public Boolean isExistsTestPlan() {
    return existsTestPlan;
  }

  public void setExistsTestPlan(Boolean existsTestPlan) {
    this.existsTestPlan = existsTestPlan;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DiaryAssignment diaryAssignment = (DiaryAssignment) o;
    return Objects.equals(this.mark, diaryAssignment.mark) &&
        Objects.equals(this.attachments, diaryAssignment.attachments) &&
        Objects.equals(this.id, diaryAssignment.id) &&
        Objects.equals(this.typeId, diaryAssignment.typeId) &&
        Objects.equals(this.assignmentName, diaryAssignment.assignmentName) &&
        Objects.equals(this.weight, diaryAssignment.weight) &&
        Objects.equals(this.dueDate, diaryAssignment.dueDate) &&
        Objects.equals(this.classMeetingId, diaryAssignment.classMeetingId) &&
        Objects.equals(this.existsTestPlan, diaryAssignment.existsTestPlan);
  }

  @Override
  public int hashCode() {
    return Objects.hash(mark, attachments, id, typeId, assignmentName, weight, dueDate, classMeetingId, existsTestPlan);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DiaryAssignment {\n");
    
    sb.append("    mark: ").append(toIndentedString(mark)).append("\n");
    sb.append("    attachments: ").append(toIndentedString(attachments)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    typeId: ").append(toIndentedString(typeId)).append("\n");
    sb.append("    assignmentName: ").append(toIndentedString(assignmentName)).append("\n");
    sb.append("    weight: ").append(toIndentedString(weight)).append("\n");
    sb.append("    dueDate: ").append(toIndentedString(dueDate)).append("\n");
    sb.append("    classMeetingId: ").append(toIndentedString(classMeetingId)).append("\n");
    sb.append("    existsTestPlan: ").append(toIndentedString(existsTestPlan)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
