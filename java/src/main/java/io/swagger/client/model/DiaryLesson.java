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
import io.swagger.client.model.DiaryAssignment;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.threeten.bp.LocalDate;
/**
 * DiaryLesson
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2022-11-06T08:52:10.951Z[GMT]")
public class DiaryLesson {
  @SerializedName("classmeetingId")
  private String classmeetingId = null;

  @SerializedName("day")
  private LocalDate day = null;

  @SerializedName("number")
  private Integer number = null;

  @SerializedName("room")
  private String room = null;

  @SerializedName("startTime")
  private String startTime = null;

  @SerializedName("endTime")
  private String endTime = null;

  @SerializedName("subjectName")
  private String subjectName = null;

  @SerializedName("assignments")
  private List<DiaryAssignment> assignments = null;

  public DiaryLesson classmeetingId(String classmeetingId) {
    this.classmeetingId = classmeetingId;
    return this;
  }

   /**
   * Get classmeetingId
   * @return classmeetingId
  **/
  @Schema(description = "")
  public String getClassmeetingId() {
    return classmeetingId;
  }

  public void setClassmeetingId(String classmeetingId) {
    this.classmeetingId = classmeetingId;
  }

  public DiaryLesson day(LocalDate day) {
    this.day = day;
    return this;
  }

   /**
   * Get day
   * @return day
  **/
  @Schema(description = "")
  public LocalDate getDay() {
    return day;
  }

  public void setDay(LocalDate day) {
    this.day = day;
  }

  public DiaryLesson number(Integer number) {
    this.number = number;
    return this;
  }

   /**
   * Get number
   * @return number
  **/
  @Schema(description = "")
  public Integer getNumber() {
    return number;
  }

  public void setNumber(Integer number) {
    this.number = number;
  }

  public DiaryLesson room(String room) {
    this.room = room;
    return this;
  }

   /**
   * Get room
   * @return room
  **/
  @Schema(description = "")
  public String getRoom() {
    return room;
  }

  public void setRoom(String room) {
    this.room = room;
  }

  public DiaryLesson startTime(String startTime) {
    this.startTime = startTime;
    return this;
  }

   /**
   * Get startTime
   * @return startTime
  **/
  @Schema(description = "")
  public String getStartTime() {
    return startTime;
  }

  public void setStartTime(String startTime) {
    this.startTime = startTime;
  }

  public DiaryLesson endTime(String endTime) {
    this.endTime = endTime;
    return this;
  }

   /**
   * Get endTime
   * @return endTime
  **/
  @Schema(description = "")
  public String getEndTime() {
    return endTime;
  }

  public void setEndTime(String endTime) {
    this.endTime = endTime;
  }

  public DiaryLesson subjectName(String subjectName) {
    this.subjectName = subjectName;
    return this;
  }

   /**
   * Get subjectName
   * @return subjectName
  **/
  @Schema(description = "")
  public String getSubjectName() {
    return subjectName;
  }

  public void setSubjectName(String subjectName) {
    this.subjectName = subjectName;
  }

  public DiaryLesson assignments(List<DiaryAssignment> assignments) {
    this.assignments = assignments;
    return this;
  }

  public DiaryLesson addAssignmentsItem(DiaryAssignment assignmentsItem) {
    if (this.assignments == null) {
      this.assignments = new ArrayList<DiaryAssignment>();
    }
    this.assignments.add(assignmentsItem);
    return this;
  }

   /**
   * Get assignments
   * @return assignments
  **/
  @Schema(description = "")
  public List<DiaryAssignment> getAssignments() {
    return assignments;
  }

  public void setAssignments(List<DiaryAssignment> assignments) {
    this.assignments = assignments;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DiaryLesson diaryLesson = (DiaryLesson) o;
    return Objects.equals(this.classmeetingId, diaryLesson.classmeetingId) &&
        Objects.equals(this.day, diaryLesson.day) &&
        Objects.equals(this.number, diaryLesson.number) &&
        Objects.equals(this.room, diaryLesson.room) &&
        Objects.equals(this.startTime, diaryLesson.startTime) &&
        Objects.equals(this.endTime, diaryLesson.endTime) &&
        Objects.equals(this.subjectName, diaryLesson.subjectName) &&
        Objects.equals(this.assignments, diaryLesson.assignments);
  }

  @Override
  public int hashCode() {
    return Objects.hash(classmeetingId, day, number, room, startTime, endTime, subjectName, assignments);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DiaryLesson {\n");
    
    sb.append("    classmeetingId: ").append(toIndentedString(classmeetingId)).append("\n");
    sb.append("    day: ").append(toIndentedString(day)).append("\n");
    sb.append("    number: ").append(toIndentedString(number)).append("\n");
    sb.append("    room: ").append(toIndentedString(room)).append("\n");
    sb.append("    startTime: ").append(toIndentedString(startTime)).append("\n");
    sb.append("    endTime: ").append(toIndentedString(endTime)).append("\n");
    sb.append("    subjectName: ").append(toIndentedString(subjectName)).append("\n");
    sb.append("    assignments: ").append(toIndentedString(assignments)).append("\n");
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
