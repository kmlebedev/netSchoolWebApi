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
    /// MySettings
    /// </summary>
    [DataContract]
        public partial class MySettings :  IEquatable<MySettings>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="MySettings" /> class.
        /// </summary>
        /// <param name="userId">userId.</param>
        /// <param name="firstName">firstName.</param>
        /// <param name="lastName">lastName.</param>
        /// <param name="middleName">middleName.</param>
        /// <param name="loginName">loginName.</param>
        /// <param name="birthDate">birthDate.</param>
        /// <param name="roles">roles.</param>
        /// <param name="schoolyearId">schoolyearId.</param>
        /// <param name="windowsAccount">windowsAccount.</param>
        /// <param name="mobilePhone">mobilePhone.</param>
        /// <param name="preferedCom">preferedCom.</param>
        /// <param name="email">email.</param>
        /// <param name="existsPhoto">existsPhoto.</param>
        /// <param name="userSettings">userSettings.</param>
        public MySettings(int? userId = default(int?), string firstName = default(string), string lastName = default(string), string middleName = default(string), string loginName = default(string), DateTime? birthDate = default(DateTime?), List<string> roles = default(List<string>), int? schoolyearId = default(int?), string windowsAccount = default(string), string mobilePhone = default(string), string preferedCom = default(string), string email = default(string), bool? existsPhoto = default(bool?), MySettingsUserSettings userSettings = default(MySettingsUserSettings))
        {
            this.UserId = userId;
            this.FirstName = firstName;
            this.LastName = lastName;
            this.MiddleName = middleName;
            this.LoginName = loginName;
            this.BirthDate = birthDate;
            this.Roles = roles;
            this.SchoolyearId = schoolyearId;
            this.WindowsAccount = windowsAccount;
            this.MobilePhone = mobilePhone;
            this.PreferedCom = preferedCom;
            this.Email = email;
            this.ExistsPhoto = existsPhoto;
            this.UserSettings = userSettings;
        }
        
        /// <summary>
        /// Gets or Sets UserId
        /// </summary>
        [DataMember(Name="userId", EmitDefaultValue=false)]
        public int? UserId { get; set; }

        /// <summary>
        /// Gets or Sets FirstName
        /// </summary>
        [DataMember(Name="firstName", EmitDefaultValue=false)]
        public string FirstName { get; set; }

        /// <summary>
        /// Gets or Sets LastName
        /// </summary>
        [DataMember(Name="lastName", EmitDefaultValue=false)]
        public string LastName { get; set; }

        /// <summary>
        /// Gets or Sets MiddleName
        /// </summary>
        [DataMember(Name="middleName", EmitDefaultValue=false)]
        public string MiddleName { get; set; }

        /// <summary>
        /// Gets or Sets LoginName
        /// </summary>
        [DataMember(Name="loginName", EmitDefaultValue=false)]
        public string LoginName { get; set; }

        /// <summary>
        /// Gets or Sets BirthDate
        /// </summary>
        [DataMember(Name="birthDate", EmitDefaultValue=false)]
        [JsonConverter(typeof(SwaggerDateConverter))]
        public DateTime? BirthDate { get; set; }

        /// <summary>
        /// Gets or Sets Roles
        /// </summary>
        [DataMember(Name="roles", EmitDefaultValue=false)]
        public List<string> Roles { get; set; }

        /// <summary>
        /// Gets or Sets SchoolyearId
        /// </summary>
        [DataMember(Name="schoolyearId", EmitDefaultValue=false)]
        public int? SchoolyearId { get; set; }

        /// <summary>
        /// Gets or Sets WindowsAccount
        /// </summary>
        [DataMember(Name="windowsAccount", EmitDefaultValue=false)]
        public string WindowsAccount { get; set; }

        /// <summary>
        /// Gets or Sets MobilePhone
        /// </summary>
        [DataMember(Name="mobilePhone", EmitDefaultValue=false)]
        public string MobilePhone { get; set; }

        /// <summary>
        /// Gets or Sets PreferedCom
        /// </summary>
        [DataMember(Name="preferedCom", EmitDefaultValue=false)]
        public string PreferedCom { get; set; }

        /// <summary>
        /// Gets or Sets Email
        /// </summary>
        [DataMember(Name="email", EmitDefaultValue=false)]
        public string Email { get; set; }

        /// <summary>
        /// Gets or Sets ExistsPhoto
        /// </summary>
        [DataMember(Name="existsPhoto", EmitDefaultValue=false)]
        public bool? ExistsPhoto { get; set; }

        /// <summary>
        /// Gets or Sets UserSettings
        /// </summary>
        [DataMember(Name="userSettings", EmitDefaultValue=false)]
        public MySettingsUserSettings UserSettings { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class MySettings {\n");
            sb.Append("  UserId: ").Append(UserId).Append("\n");
            sb.Append("  FirstName: ").Append(FirstName).Append("\n");
            sb.Append("  LastName: ").Append(LastName).Append("\n");
            sb.Append("  MiddleName: ").Append(MiddleName).Append("\n");
            sb.Append("  LoginName: ").Append(LoginName).Append("\n");
            sb.Append("  BirthDate: ").Append(BirthDate).Append("\n");
            sb.Append("  Roles: ").Append(Roles).Append("\n");
            sb.Append("  SchoolyearId: ").Append(SchoolyearId).Append("\n");
            sb.Append("  WindowsAccount: ").Append(WindowsAccount).Append("\n");
            sb.Append("  MobilePhone: ").Append(MobilePhone).Append("\n");
            sb.Append("  PreferedCom: ").Append(PreferedCom).Append("\n");
            sb.Append("  Email: ").Append(Email).Append("\n");
            sb.Append("  ExistsPhoto: ").Append(ExistsPhoto).Append("\n");
            sb.Append("  UserSettings: ").Append(UserSettings).Append("\n");
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
            return this.Equals(input as MySettings);
        }

        /// <summary>
        /// Returns true if MySettings instances are equal
        /// </summary>
        /// <param name="input">Instance of MySettings to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(MySettings input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.UserId == input.UserId ||
                    (this.UserId != null &&
                    this.UserId.Equals(input.UserId))
                ) && 
                (
                    this.FirstName == input.FirstName ||
                    (this.FirstName != null &&
                    this.FirstName.Equals(input.FirstName))
                ) && 
                (
                    this.LastName == input.LastName ||
                    (this.LastName != null &&
                    this.LastName.Equals(input.LastName))
                ) && 
                (
                    this.MiddleName == input.MiddleName ||
                    (this.MiddleName != null &&
                    this.MiddleName.Equals(input.MiddleName))
                ) && 
                (
                    this.LoginName == input.LoginName ||
                    (this.LoginName != null &&
                    this.LoginName.Equals(input.LoginName))
                ) && 
                (
                    this.BirthDate == input.BirthDate ||
                    (this.BirthDate != null &&
                    this.BirthDate.Equals(input.BirthDate))
                ) && 
                (
                    this.Roles == input.Roles ||
                    this.Roles != null &&
                    input.Roles != null &&
                    this.Roles.SequenceEqual(input.Roles)
                ) && 
                (
                    this.SchoolyearId == input.SchoolyearId ||
                    (this.SchoolyearId != null &&
                    this.SchoolyearId.Equals(input.SchoolyearId))
                ) && 
                (
                    this.WindowsAccount == input.WindowsAccount ||
                    (this.WindowsAccount != null &&
                    this.WindowsAccount.Equals(input.WindowsAccount))
                ) && 
                (
                    this.MobilePhone == input.MobilePhone ||
                    (this.MobilePhone != null &&
                    this.MobilePhone.Equals(input.MobilePhone))
                ) && 
                (
                    this.PreferedCom == input.PreferedCom ||
                    (this.PreferedCom != null &&
                    this.PreferedCom.Equals(input.PreferedCom))
                ) && 
                (
                    this.Email == input.Email ||
                    (this.Email != null &&
                    this.Email.Equals(input.Email))
                ) && 
                (
                    this.ExistsPhoto == input.ExistsPhoto ||
                    (this.ExistsPhoto != null &&
                    this.ExistsPhoto.Equals(input.ExistsPhoto))
                ) && 
                (
                    this.UserSettings == input.UserSettings ||
                    (this.UserSettings != null &&
                    this.UserSettings.Equals(input.UserSettings))
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
                if (this.UserId != null)
                    hashCode = hashCode * 59 + this.UserId.GetHashCode();
                if (this.FirstName != null)
                    hashCode = hashCode * 59 + this.FirstName.GetHashCode();
                if (this.LastName != null)
                    hashCode = hashCode * 59 + this.LastName.GetHashCode();
                if (this.MiddleName != null)
                    hashCode = hashCode * 59 + this.MiddleName.GetHashCode();
                if (this.LoginName != null)
                    hashCode = hashCode * 59 + this.LoginName.GetHashCode();
                if (this.BirthDate != null)
                    hashCode = hashCode * 59 + this.BirthDate.GetHashCode();
                if (this.Roles != null)
                    hashCode = hashCode * 59 + this.Roles.GetHashCode();
                if (this.SchoolyearId != null)
                    hashCode = hashCode * 59 + this.SchoolyearId.GetHashCode();
                if (this.WindowsAccount != null)
                    hashCode = hashCode * 59 + this.WindowsAccount.GetHashCode();
                if (this.MobilePhone != null)
                    hashCode = hashCode * 59 + this.MobilePhone.GetHashCode();
                if (this.PreferedCom != null)
                    hashCode = hashCode * 59 + this.PreferedCom.GetHashCode();
                if (this.Email != null)
                    hashCode = hashCode * 59 + this.Email.GetHashCode();
                if (this.ExistsPhoto != null)
                    hashCode = hashCode * 59 + this.ExistsPhoto.GetHashCode();
                if (this.UserSettings != null)
                    hashCode = hashCode * 59 + this.UserSettings.GetHashCode();
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
