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
 * LoginData
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2022-10-16T17:55:39.713Z[GMT]")
public class LoginData {
  @SerializedName("productName")
  private String productName = null;

  @SerializedName("version")
  private String version = null;

  @SerializedName("schoolLogin")
  private Boolean schoolLogin = null;

  @SerializedName("emLogin")
  private Boolean emLogin = null;

  @SerializedName("esiaLogin")
  private Boolean esiaLogin = null;

  @SerializedName("esiaLoginPage")
  private String esiaLoginPage = null;

  @SerializedName("esiaMainAuth")
  private Boolean esiaMainAuth = null;

  @SerializedName("esiaButton")
  private Boolean esiaButton = null;

  @SerializedName("signatureLogin")
  private Boolean signatureLogin = null;

  @SerializedName("cacheVer")
  private String cacheVer = null;

  @SerializedName("windowsAuth")
  private Boolean windowsAuth = null;

  @SerializedName("enableSms")
  private Boolean enableSms = null;

  @SerializedName("esaLogin")
  private Boolean esaLogin = null;

  @SerializedName("esaLoginPage")
  private String esaLoginPage = null;

  public LoginData productName(String productName) {
    this.productName = productName;
    return this;
  }

   /**
   * Get productName
   * @return productName
  **/
  @Schema(description = "")
  public String getProductName() {
    return productName;
  }

  public void setProductName(String productName) {
    this.productName = productName;
  }

  public LoginData version(String version) {
    this.version = version;
    return this;
  }

   /**
   * Get version
   * @return version
  **/
  @Schema(description = "")
  public String getVersion() {
    return version;
  }

  public void setVersion(String version) {
    this.version = version;
  }

  public LoginData schoolLogin(Boolean schoolLogin) {
    this.schoolLogin = schoolLogin;
    return this;
  }

   /**
   * Get schoolLogin
   * @return schoolLogin
  **/
  @Schema(description = "")
  public Boolean isSchoolLogin() {
    return schoolLogin;
  }

  public void setSchoolLogin(Boolean schoolLogin) {
    this.schoolLogin = schoolLogin;
  }

  public LoginData emLogin(Boolean emLogin) {
    this.emLogin = emLogin;
    return this;
  }

   /**
   * Get emLogin
   * @return emLogin
  **/
  @Schema(description = "")
  public Boolean isEmLogin() {
    return emLogin;
  }

  public void setEmLogin(Boolean emLogin) {
    this.emLogin = emLogin;
  }

  public LoginData esiaLogin(Boolean esiaLogin) {
    this.esiaLogin = esiaLogin;
    return this;
  }

   /**
   * Get esiaLogin
   * @return esiaLogin
  **/
  @Schema(description = "")
  public Boolean isEsiaLogin() {
    return esiaLogin;
  }

  public void setEsiaLogin(Boolean esiaLogin) {
    this.esiaLogin = esiaLogin;
  }

  public LoginData esiaLoginPage(String esiaLoginPage) {
    this.esiaLoginPage = esiaLoginPage;
    return this;
  }

   /**
   * Get esiaLoginPage
   * @return esiaLoginPage
  **/
  @Schema(description = "")
  public String getEsiaLoginPage() {
    return esiaLoginPage;
  }

  public void setEsiaLoginPage(String esiaLoginPage) {
    this.esiaLoginPage = esiaLoginPage;
  }

  public LoginData esiaMainAuth(Boolean esiaMainAuth) {
    this.esiaMainAuth = esiaMainAuth;
    return this;
  }

   /**
   * Get esiaMainAuth
   * @return esiaMainAuth
  **/
  @Schema(description = "")
  public Boolean isEsiaMainAuth() {
    return esiaMainAuth;
  }

  public void setEsiaMainAuth(Boolean esiaMainAuth) {
    this.esiaMainAuth = esiaMainAuth;
  }

  public LoginData esiaButton(Boolean esiaButton) {
    this.esiaButton = esiaButton;
    return this;
  }

   /**
   * Get esiaButton
   * @return esiaButton
  **/
  @Schema(description = "")
  public Boolean isEsiaButton() {
    return esiaButton;
  }

  public void setEsiaButton(Boolean esiaButton) {
    this.esiaButton = esiaButton;
  }

  public LoginData signatureLogin(Boolean signatureLogin) {
    this.signatureLogin = signatureLogin;
    return this;
  }

   /**
   * Get signatureLogin
   * @return signatureLogin
  **/
  @Schema(description = "")
  public Boolean isSignatureLogin() {
    return signatureLogin;
  }

  public void setSignatureLogin(Boolean signatureLogin) {
    this.signatureLogin = signatureLogin;
  }

  public LoginData cacheVer(String cacheVer) {
    this.cacheVer = cacheVer;
    return this;
  }

   /**
   * Get cacheVer
   * @return cacheVer
  **/
  @Schema(description = "")
  public String getCacheVer() {
    return cacheVer;
  }

  public void setCacheVer(String cacheVer) {
    this.cacheVer = cacheVer;
  }

  public LoginData windowsAuth(Boolean windowsAuth) {
    this.windowsAuth = windowsAuth;
    return this;
  }

   /**
   * Get windowsAuth
   * @return windowsAuth
  **/
  @Schema(description = "")
  public Boolean isWindowsAuth() {
    return windowsAuth;
  }

  public void setWindowsAuth(Boolean windowsAuth) {
    this.windowsAuth = windowsAuth;
  }

  public LoginData enableSms(Boolean enableSms) {
    this.enableSms = enableSms;
    return this;
  }

   /**
   * Get enableSms
   * @return enableSms
  **/
  @Schema(description = "")
  public Boolean isEnableSms() {
    return enableSms;
  }

  public void setEnableSms(Boolean enableSms) {
    this.enableSms = enableSms;
  }

  public LoginData esaLogin(Boolean esaLogin) {
    this.esaLogin = esaLogin;
    return this;
  }

   /**
   * Get esaLogin
   * @return esaLogin
  **/
  @Schema(description = "")
  public Boolean isEsaLogin() {
    return esaLogin;
  }

  public void setEsaLogin(Boolean esaLogin) {
    this.esaLogin = esaLogin;
  }

  public LoginData esaLoginPage(String esaLoginPage) {
    this.esaLoginPage = esaLoginPage;
    return this;
  }

   /**
   * Get esaLoginPage
   * @return esaLoginPage
  **/
  @Schema(description = "")
  public String getEsaLoginPage() {
    return esaLoginPage;
  }

  public void setEsaLoginPage(String esaLoginPage) {
    this.esaLoginPage = esaLoginPage;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LoginData loginData = (LoginData) o;
    return Objects.equals(this.productName, loginData.productName) &&
        Objects.equals(this.version, loginData.version) &&
        Objects.equals(this.schoolLogin, loginData.schoolLogin) &&
        Objects.equals(this.emLogin, loginData.emLogin) &&
        Objects.equals(this.esiaLogin, loginData.esiaLogin) &&
        Objects.equals(this.esiaLoginPage, loginData.esiaLoginPage) &&
        Objects.equals(this.esiaMainAuth, loginData.esiaMainAuth) &&
        Objects.equals(this.esiaButton, loginData.esiaButton) &&
        Objects.equals(this.signatureLogin, loginData.signatureLogin) &&
        Objects.equals(this.cacheVer, loginData.cacheVer) &&
        Objects.equals(this.windowsAuth, loginData.windowsAuth) &&
        Objects.equals(this.enableSms, loginData.enableSms) &&
        Objects.equals(this.esaLogin, loginData.esaLogin) &&
        Objects.equals(this.esaLoginPage, loginData.esaLoginPage);
  }

  @Override
  public int hashCode() {
    return Objects.hash(productName, version, schoolLogin, emLogin, esiaLogin, esiaLoginPage, esiaMainAuth, esiaButton, signatureLogin, cacheVer, windowsAuth, enableSms, esaLogin, esaLoginPage);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LoginData {\n");
    
    sb.append("    productName: ").append(toIndentedString(productName)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
    sb.append("    schoolLogin: ").append(toIndentedString(schoolLogin)).append("\n");
    sb.append("    emLogin: ").append(toIndentedString(emLogin)).append("\n");
    sb.append("    esiaLogin: ").append(toIndentedString(esiaLogin)).append("\n");
    sb.append("    esiaLoginPage: ").append(toIndentedString(esiaLoginPage)).append("\n");
    sb.append("    esiaMainAuth: ").append(toIndentedString(esiaMainAuth)).append("\n");
    sb.append("    esiaButton: ").append(toIndentedString(esiaButton)).append("\n");
    sb.append("    signatureLogin: ").append(toIndentedString(signatureLogin)).append("\n");
    sb.append("    cacheVer: ").append(toIndentedString(cacheVer)).append("\n");
    sb.append("    windowsAuth: ").append(toIndentedString(windowsAuth)).append("\n");
    sb.append("    enableSms: ").append(toIndentedString(enableSms)).append("\n");
    sb.append("    esaLogin: ").append(toIndentedString(esaLogin)).append("\n");
    sb.append("    esaLoginPage: ").append(toIndentedString(esaLoginPage)).append("\n");
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
