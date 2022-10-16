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
 * DiaryAssignDetailsTeacher
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2022-10-16T17:55:39.713Z[GMT]")
public class DiaryAssignDetailsTeacher {
  @SerializedName("id")
  private Integer id = null;

  @SerializedName("name")
  private String name = null;

  public DiaryAssignDetailsTeacher id(Integer id) {
    this.id = id;
    return this;
  }

   /**
   * Get id
   * @return id
  **/
  @Schema(example = "71111", description = "")
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }

  public DiaryAssignDetailsTeacher name(String name) {
    this.name = name;
    return this;
  }

   /**
   * Get name
   * @return name
  **/
  @Schema(example = "Иванова Марья Ивановна", description = "")
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DiaryAssignDetailsTeacher diaryAssignDetailsTeacher = (DiaryAssignDetailsTeacher) o;
    return Objects.equals(this.id, diaryAssignDetailsTeacher.id) &&
        Objects.equals(this.name, diaryAssignDetailsTeacher.name);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, name);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DiaryAssignDetailsTeacher {\n");
    
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
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
