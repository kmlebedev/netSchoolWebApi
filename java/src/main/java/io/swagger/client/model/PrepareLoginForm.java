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
import io.swagger.client.model.PrepareEmLoginFormCountries;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
/**
 * PrepareLoginForm
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2022-10-24T12:37:15.210Z[GMT]")
public class PrepareLoginForm {
  @SerializedName("countries")
  private List<PrepareEmLoginFormCountries> countries = null;

  @SerializedName("states")
  private List<PrepareEmLoginFormCountries> states = null;

  @SerializedName("provinces")
  private List<PrepareEmLoginFormCountries> provinces = null;

  @SerializedName("cities")
  private List<PrepareEmLoginFormCountries> cities = null;

  @SerializedName("funcs")
  private List<PrepareEmLoginFormCountries> funcs = null;

  @SerializedName("schools")
  private List<PrepareEmLoginFormCountries> schools = null;

  @SerializedName("cid")
  private Integer cid = null;

  @SerializedName("sid")
  private Integer sid = null;

  @SerializedName("pid")
  private Integer pid = null;

  @SerializedName("cn")
  private Integer cn = null;

  @SerializedName("sft")
  private Integer sft = null;

  @SerializedName("scid")
  private Integer scid = null;

  @SerializedName("hlevels")
  private Object hlevels = null;

  @SerializedName("ems")
  private Object ems = null;

  public PrepareLoginForm countries(List<PrepareEmLoginFormCountries> countries) {
    this.countries = countries;
    return this;
  }

  public PrepareLoginForm addCountriesItem(PrepareEmLoginFormCountries countriesItem) {
    if (this.countries == null) {
      this.countries = new ArrayList<PrepareEmLoginFormCountries>();
    }
    this.countries.add(countriesItem);
    return this;
  }

   /**
   * Get countries
   * @return countries
  **/
  @Schema(description = "")
  public List<PrepareEmLoginFormCountries> getCountries() {
    return countries;
  }

  public void setCountries(List<PrepareEmLoginFormCountries> countries) {
    this.countries = countries;
  }

  public PrepareLoginForm states(List<PrepareEmLoginFormCountries> states) {
    this.states = states;
    return this;
  }

  public PrepareLoginForm addStatesItem(PrepareEmLoginFormCountries statesItem) {
    if (this.states == null) {
      this.states = new ArrayList<PrepareEmLoginFormCountries>();
    }
    this.states.add(statesItem);
    return this;
  }

   /**
   * Get states
   * @return states
  **/
  @Schema(description = "")
  public List<PrepareEmLoginFormCountries> getStates() {
    return states;
  }

  public void setStates(List<PrepareEmLoginFormCountries> states) {
    this.states = states;
  }

  public PrepareLoginForm provinces(List<PrepareEmLoginFormCountries> provinces) {
    this.provinces = provinces;
    return this;
  }

  public PrepareLoginForm addProvincesItem(PrepareEmLoginFormCountries provincesItem) {
    if (this.provinces == null) {
      this.provinces = new ArrayList<PrepareEmLoginFormCountries>();
    }
    this.provinces.add(provincesItem);
    return this;
  }

   /**
   * Get provinces
   * @return provinces
  **/
  @Schema(description = "")
  public List<PrepareEmLoginFormCountries> getProvinces() {
    return provinces;
  }

  public void setProvinces(List<PrepareEmLoginFormCountries> provinces) {
    this.provinces = provinces;
  }

  public PrepareLoginForm cities(List<PrepareEmLoginFormCountries> cities) {
    this.cities = cities;
    return this;
  }

  public PrepareLoginForm addCitiesItem(PrepareEmLoginFormCountries citiesItem) {
    if (this.cities == null) {
      this.cities = new ArrayList<PrepareEmLoginFormCountries>();
    }
    this.cities.add(citiesItem);
    return this;
  }

   /**
   * Get cities
   * @return cities
  **/
  @Schema(description = "")
  public List<PrepareEmLoginFormCountries> getCities() {
    return cities;
  }

  public void setCities(List<PrepareEmLoginFormCountries> cities) {
    this.cities = cities;
  }

  public PrepareLoginForm funcs(List<PrepareEmLoginFormCountries> funcs) {
    this.funcs = funcs;
    return this;
  }

  public PrepareLoginForm addFuncsItem(PrepareEmLoginFormCountries funcsItem) {
    if (this.funcs == null) {
      this.funcs = new ArrayList<PrepareEmLoginFormCountries>();
    }
    this.funcs.add(funcsItem);
    return this;
  }

   /**
   * Get funcs
   * @return funcs
  **/
  @Schema(description = "")
  public List<PrepareEmLoginFormCountries> getFuncs() {
    return funcs;
  }

  public void setFuncs(List<PrepareEmLoginFormCountries> funcs) {
    this.funcs = funcs;
  }

  public PrepareLoginForm schools(List<PrepareEmLoginFormCountries> schools) {
    this.schools = schools;
    return this;
  }

  public PrepareLoginForm addSchoolsItem(PrepareEmLoginFormCountries schoolsItem) {
    if (this.schools == null) {
      this.schools = new ArrayList<PrepareEmLoginFormCountries>();
    }
    this.schools.add(schoolsItem);
    return this;
  }

   /**
   * Get schools
   * @return schools
  **/
  @Schema(description = "")
  public List<PrepareEmLoginFormCountries> getSchools() {
    return schools;
  }

  public void setSchools(List<PrepareEmLoginFormCountries> schools) {
    this.schools = schools;
  }

  public PrepareLoginForm cid(Integer cid) {
    this.cid = cid;
    return this;
  }

   /**
   * Get cid
   * @return cid
  **/
  @Schema(description = "")
  public Integer getCid() {
    return cid;
  }

  public void setCid(Integer cid) {
    this.cid = cid;
  }

  public PrepareLoginForm sid(Integer sid) {
    this.sid = sid;
    return this;
  }

   /**
   * Get sid
   * @return sid
  **/
  @Schema(description = "")
  public Integer getSid() {
    return sid;
  }

  public void setSid(Integer sid) {
    this.sid = sid;
  }

  public PrepareLoginForm pid(Integer pid) {
    this.pid = pid;
    return this;
  }

   /**
   * Get pid
   * @return pid
  **/
  @Schema(description = "")
  public Integer getPid() {
    return pid;
  }

  public void setPid(Integer pid) {
    this.pid = pid;
  }

  public PrepareLoginForm cn(Integer cn) {
    this.cn = cn;
    return this;
  }

   /**
   * Get cn
   * @return cn
  **/
  @Schema(description = "")
  public Integer getCn() {
    return cn;
  }

  public void setCn(Integer cn) {
    this.cn = cn;
  }

  public PrepareLoginForm sft(Integer sft) {
    this.sft = sft;
    return this;
  }

   /**
   * Get sft
   * @return sft
  **/
  @Schema(description = "")
  public Integer getSft() {
    return sft;
  }

  public void setSft(Integer sft) {
    this.sft = sft;
  }

  public PrepareLoginForm scid(Integer scid) {
    this.scid = scid;
    return this;
  }

   /**
   * Get scid
   * @return scid
  **/
  @Schema(description = "")
  public Integer getScid() {
    return scid;
  }

  public void setScid(Integer scid) {
    this.scid = scid;
  }

  public PrepareLoginForm hlevels(Object hlevels) {
    this.hlevels = hlevels;
    return this;
  }

   /**
   * Get hlevels
   * @return hlevels
  **/
  @Schema(description = "")
  public Object getHlevels() {
    return hlevels;
  }

  public void setHlevels(Object hlevels) {
    this.hlevels = hlevels;
  }

  public PrepareLoginForm ems(Object ems) {
    this.ems = ems;
    return this;
  }

   /**
   * Get ems
   * @return ems
  **/
  @Schema(description = "")
  public Object getEms() {
    return ems;
  }

  public void setEms(Object ems) {
    this.ems = ems;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PrepareLoginForm prepareLoginForm = (PrepareLoginForm) o;
    return Objects.equals(this.countries, prepareLoginForm.countries) &&
        Objects.equals(this.states, prepareLoginForm.states) &&
        Objects.equals(this.provinces, prepareLoginForm.provinces) &&
        Objects.equals(this.cities, prepareLoginForm.cities) &&
        Objects.equals(this.funcs, prepareLoginForm.funcs) &&
        Objects.equals(this.schools, prepareLoginForm.schools) &&
        Objects.equals(this.cid, prepareLoginForm.cid) &&
        Objects.equals(this.sid, prepareLoginForm.sid) &&
        Objects.equals(this.pid, prepareLoginForm.pid) &&
        Objects.equals(this.cn, prepareLoginForm.cn) &&
        Objects.equals(this.sft, prepareLoginForm.sft) &&
        Objects.equals(this.scid, prepareLoginForm.scid) &&
        Objects.equals(this.hlevels, prepareLoginForm.hlevels) &&
        Objects.equals(this.ems, prepareLoginForm.ems);
  }

  @Override
  public int hashCode() {
    return Objects.hash(countries, states, provinces, cities, funcs, schools, cid, sid, pid, cn, sft, scid, hlevels, ems);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PrepareLoginForm {\n");
    
    sb.append("    countries: ").append(toIndentedString(countries)).append("\n");
    sb.append("    states: ").append(toIndentedString(states)).append("\n");
    sb.append("    provinces: ").append(toIndentedString(provinces)).append("\n");
    sb.append("    cities: ").append(toIndentedString(cities)).append("\n");
    sb.append("    funcs: ").append(toIndentedString(funcs)).append("\n");
    sb.append("    schools: ").append(toIndentedString(schools)).append("\n");
    sb.append("    cid: ").append(toIndentedString(cid)).append("\n");
    sb.append("    sid: ").append(toIndentedString(sid)).append("\n");
    sb.append("    pid: ").append(toIndentedString(pid)).append("\n");
    sb.append("    cn: ").append(toIndentedString(cn)).append("\n");
    sb.append("    sft: ").append(toIndentedString(sft)).append("\n");
    sb.append("    scid: ").append(toIndentedString(scid)).append("\n");
    sb.append("    hlevels: ").append(toIndentedString(hlevels)).append("\n");
    sb.append("    ems: ").append(toIndentedString(ems)).append("\n");
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
