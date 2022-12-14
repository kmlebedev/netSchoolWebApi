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
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
/**
 * Mark
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2022-11-06T08:52:10.951Z[GMT]")
public class Mark {
  @SerializedName("assignmentId")
  private Integer assignmentId = null;

  @SerializedName("studentId")
  private Integer studentId = null;

  @SerializedName("mark")
  private Integer mark = null;

  @SerializedName("dutyMark")
  private Boolean dutyMark = null;

  public Mark assignmentId(Integer assignmentId) {
    this.assignmentId = assignmentId;
    return this;
  }

   /**
   * Get assignmentId
   * @return assignmentId
  **/
  @Schema(description = "")
  public Integer getAssignmentId() {
    return assignmentId;
  }

  public void setAssignmentId(Integer assignmentId) {
    this.assignmentId = assignmentId;
  }

  public Mark studentId(Integer studentId) {
    this.studentId = studentId;
    return this;
  }

   /**
   * Get studentId
   * @return studentId
  **/
  @Schema(description = "")
  public Integer getStudentId() {
    return studentId;
  }

  public void setStudentId(Integer studentId) {
    this.studentId = studentId;
  }

  public Mark mark(Integer mark) {
    this.mark = mark;
    return this;
  }

   /**
   * Get mark
   * @return mark
  **/
  @Schema(description = "")
  public Integer getMark() {
    return mark;
  }

  public void setMark(Integer mark) {
    this.mark = mark;
  }

  public Mark dutyMark(Boolean dutyMark) {
    this.dutyMark = dutyMark;
    return this;
  }

   /**
   * Get dutyMark
   * @return dutyMark
  **/
  @Schema(description = "")
  public Boolean isDutyMark() {
    return dutyMark;
  }

  public void setDutyMark(Boolean dutyMark) {
    this.dutyMark = dutyMark;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Mark mark = (Mark) o;
    return Objects.equals(this.assignmentId, mark.assignmentId) &&
        Objects.equals(this.studentId, mark.studentId) &&
        Objects.equals(this.mark, mark.mark) &&
        Objects.equals(this.dutyMark, mark.dutyMark);
  }

  @Override
  public int hashCode() {
    return Objects.hash(assignmentId, studentId, mark, dutyMark);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Mark {\n");
    
    sb.append("    assignmentId: ").append(toIndentedString(assignmentId)).append("\n");
    sb.append("    studentId: ").append(toIndentedString(studentId)).append("\n");
    sb.append("    mark: ").append(toIndentedString(mark)).append("\n");
    sb.append("    dutyMark: ").append(toIndentedString(dutyMark)).append("\n");
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
