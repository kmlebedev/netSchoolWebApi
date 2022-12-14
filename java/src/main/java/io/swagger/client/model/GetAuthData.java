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
 * GetAuthData
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2022-11-06T08:52:10.951Z[GMT]")
public class GetAuthData {
  @SerializedName("lt")
  private String lt = null;

  @SerializedName("ver")
  private String ver = null;

  @SerializedName("salt")
  private String salt = null;

  public GetAuthData lt(String lt) {
    this.lt = lt;
    return this;
  }

   /**
   * Get lt
   * @return lt
  **/
  @Schema(example = "1073163840", description = "")
  public String getLt() {
    return lt;
  }

  public void setLt(String lt) {
    this.lt = lt;
  }

  public GetAuthData ver(String ver) {
    this.ver = ver;
    return this;
  }

   /**
   * Get ver
   * @return ver
  **/
  @Schema(example = "768253229", description = "")
  public String getVer() {
    return ver;
  }

  public void setVer(String ver) {
    this.ver = ver;
  }

  public GetAuthData salt(String salt) {
    this.salt = salt;
    return this;
  }

   /**
   * Get salt
   * @return salt
  **/
  @Schema(example = "1458933352", description = "")
  public String getSalt() {
    return salt;
  }

  public void setSalt(String salt) {
    this.salt = salt;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetAuthData getAuthData = (GetAuthData) o;
    return Objects.equals(this.lt, getAuthData.lt) &&
        Objects.equals(this.ver, getAuthData.ver) &&
        Objects.equals(this.salt, getAuthData.salt);
  }

  @Override
  public int hashCode() {
    return Objects.hash(lt, ver, salt);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetAuthData {\n");
    
    sb.append("    lt: ").append(toIndentedString(lt)).append("\n");
    sb.append("    ver: ").append(toIndentedString(ver)).append("\n");
    sb.append("    salt: ").append(toIndentedString(salt)).append("\n");
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
