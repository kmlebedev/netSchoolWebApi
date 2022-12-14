/* 
 * NetSchool
 *
 * The API for the NetSchool irTech project
 *
 * OpenAPI spec version: 5.10.63221
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */
using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = IO.Swagger.Client.SwaggerDateConverter;

namespace IO.Swagger.Model
{
    /// <summary>
    /// LoginAccountInfo
    /// </summary>
    [DataContract]
        public partial class LoginAccountInfo :  IEquatable<LoginAccountInfo>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="LoginAccountInfo" /> class.
        /// </summary>
        /// <param name="activeToken">activeToken.</param>
        /// <param name="secureActiveToken">secureActiveToken.</param>
        /// <param name="currentOrganization">currentOrganization.</param>
        /// <param name="user">user.</param>
        /// <param name="userRoles">userRoles.</param>
        /// <param name="organizations">organizations.</param>
        /// <param name="loginTime">loginTime.</param>
        /// <param name="active">active.</param>
        /// <param name="canLogin">canLogin.</param>
        /// <param name="storeTokens">storeTokens.</param>
        /// <param name="accessToken">accessToken.</param>
        public LoginAccountInfo(string activeToken = default(string), string secureActiveToken = default(string), LoginAccountInfoCurrentOrganization currentOrganization = default(LoginAccountInfoCurrentOrganization), LoginAccountInfoUser user = default(LoginAccountInfoUser), LoginAccountInfoUserRoles userRoles = default(LoginAccountInfoUserRoles), List<LoginAccountInfoOrganizations> organizations = default(List<LoginAccountInfoOrganizations>), DateTime? loginTime = default(DateTime?), bool? active = default(bool?), bool? canLogin = default(bool?), bool? storeTokens = default(bool?), string accessToken = default(string))
        {
            this.ActiveToken = activeToken;
            this.SecureActiveToken = secureActiveToken;
            this.CurrentOrganization = currentOrganization;
            this.User = user;
            this.UserRoles = userRoles;
            this.Organizations = organizations;
            this.LoginTime = loginTime;
            this.Active = active;
            this.CanLogin = canLogin;
            this.StoreTokens = storeTokens;
            this.AccessToken = accessToken;
        }
        
        /// <summary>
        /// Gets or Sets ActiveToken
        /// </summary>
        [DataMember(Name="activeToken", EmitDefaultValue=false)]
        public string ActiveToken { get; set; }

        /// <summary>
        /// Gets or Sets SecureActiveToken
        /// </summary>
        [DataMember(Name="secureActiveToken", EmitDefaultValue=false)]
        public string SecureActiveToken { get; set; }

        /// <summary>
        /// Gets or Sets CurrentOrganization
        /// </summary>
        [DataMember(Name="currentOrganization", EmitDefaultValue=false)]
        public LoginAccountInfoCurrentOrganization CurrentOrganization { get; set; }

        /// <summary>
        /// Gets or Sets User
        /// </summary>
        [DataMember(Name="user", EmitDefaultValue=false)]
        public LoginAccountInfoUser User { get; set; }

        /// <summary>
        /// Gets or Sets UserRoles
        /// </summary>
        [DataMember(Name="userRoles", EmitDefaultValue=false)]
        public LoginAccountInfoUserRoles UserRoles { get; set; }

        /// <summary>
        /// Gets or Sets Organizations
        /// </summary>
        [DataMember(Name="organizations", EmitDefaultValue=false)]
        public List<LoginAccountInfoOrganizations> Organizations { get; set; }

        /// <summary>
        /// Gets or Sets LoginTime
        /// </summary>
        [DataMember(Name="loginTime", EmitDefaultValue=false)]
        [JsonConverter(typeof(SwaggerDateConverter))]
        public DateTime? LoginTime { get; set; }

        /// <summary>
        /// Gets or Sets Active
        /// </summary>
        [DataMember(Name="active", EmitDefaultValue=false)]
        public bool? Active { get; set; }

        /// <summary>
        /// Gets or Sets CanLogin
        /// </summary>
        [DataMember(Name="canLogin", EmitDefaultValue=false)]
        public bool? CanLogin { get; set; }

        /// <summary>
        /// Gets or Sets StoreTokens
        /// </summary>
        [DataMember(Name="storeTokens", EmitDefaultValue=false)]
        public bool? StoreTokens { get; set; }

        /// <summary>
        /// Gets or Sets AccessToken
        /// </summary>
        [DataMember(Name="accessToken", EmitDefaultValue=false)]
        public string AccessToken { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class LoginAccountInfo {\n");
            sb.Append("  ActiveToken: ").Append(ActiveToken).Append("\n");
            sb.Append("  SecureActiveToken: ").Append(SecureActiveToken).Append("\n");
            sb.Append("  CurrentOrganization: ").Append(CurrentOrganization).Append("\n");
            sb.Append("  User: ").Append(User).Append("\n");
            sb.Append("  UserRoles: ").Append(UserRoles).Append("\n");
            sb.Append("  Organizations: ").Append(Organizations).Append("\n");
            sb.Append("  LoginTime: ").Append(LoginTime).Append("\n");
            sb.Append("  Active: ").Append(Active).Append("\n");
            sb.Append("  CanLogin: ").Append(CanLogin).Append("\n");
            sb.Append("  StoreTokens: ").Append(StoreTokens).Append("\n");
            sb.Append("  AccessToken: ").Append(AccessToken).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as LoginAccountInfo);
        }

        /// <summary>
        /// Returns true if LoginAccountInfo instances are equal
        /// </summary>
        /// <param name="input">Instance of LoginAccountInfo to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(LoginAccountInfo input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.ActiveToken == input.ActiveToken ||
                    (this.ActiveToken != null &&
                    this.ActiveToken.Equals(input.ActiveToken))
                ) && 
                (
                    this.SecureActiveToken == input.SecureActiveToken ||
                    (this.SecureActiveToken != null &&
                    this.SecureActiveToken.Equals(input.SecureActiveToken))
                ) && 
                (
                    this.CurrentOrganization == input.CurrentOrganization ||
                    (this.CurrentOrganization != null &&
                    this.CurrentOrganization.Equals(input.CurrentOrganization))
                ) && 
                (
                    this.User == input.User ||
                    (this.User != null &&
                    this.User.Equals(input.User))
                ) && 
                (
                    this.UserRoles == input.UserRoles ||
                    (this.UserRoles != null &&
                    this.UserRoles.Equals(input.UserRoles))
                ) && 
                (
                    this.Organizations == input.Organizations ||
                    this.Organizations != null &&
                    input.Organizations != null &&
                    this.Organizations.SequenceEqual(input.Organizations)
                ) && 
                (
                    this.LoginTime == input.LoginTime ||
                    (this.LoginTime != null &&
                    this.LoginTime.Equals(input.LoginTime))
                ) && 
                (
                    this.Active == input.Active ||
                    (this.Active != null &&
                    this.Active.Equals(input.Active))
                ) && 
                (
                    this.CanLogin == input.CanLogin ||
                    (this.CanLogin != null &&
                    this.CanLogin.Equals(input.CanLogin))
                ) && 
                (
                    this.StoreTokens == input.StoreTokens ||
                    (this.StoreTokens != null &&
                    this.StoreTokens.Equals(input.StoreTokens))
                ) && 
                (
                    this.AccessToken == input.AccessToken ||
                    (this.AccessToken != null &&
                    this.AccessToken.Equals(input.AccessToken))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.ActiveToken != null)
                    hashCode = hashCode * 59 + this.ActiveToken.GetHashCode();
                if (this.SecureActiveToken != null)
                    hashCode = hashCode * 59 + this.SecureActiveToken.GetHashCode();
                if (this.CurrentOrganization != null)
                    hashCode = hashCode * 59 + this.CurrentOrganization.GetHashCode();
                if (this.User != null)
                    hashCode = hashCode * 59 + this.User.GetHashCode();
                if (this.UserRoles != null)
                    hashCode = hashCode * 59 + this.UserRoles.GetHashCode();
                if (this.Organizations != null)
                    hashCode = hashCode * 59 + this.Organizations.GetHashCode();
                if (this.LoginTime != null)
                    hashCode = hashCode * 59 + this.LoginTime.GetHashCode();
                if (this.Active != null)
                    hashCode = hashCode * 59 + this.Active.GetHashCode();
                if (this.CanLogin != null)
                    hashCode = hashCode * 59 + this.CanLogin.GetHashCode();
                if (this.StoreTokens != null)
                    hashCode = hashCode * 59 + this.StoreTokens.GetHashCode();
                if (this.AccessToken != null)
                    hashCode = hashCode * 59 + this.AccessToken.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }
}
