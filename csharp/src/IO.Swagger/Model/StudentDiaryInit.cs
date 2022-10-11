/* 
 * NetSchool
 *
 * The API for the NetSchool irTech project
 *
 * OpenAPI spec version: 4.30.43656
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
    /// StudentDiaryInit
    /// </summary>
    [DataContract]
        public partial class StudentDiaryInit :  IEquatable<StudentDiaryInit>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="StudentDiaryInit" /> class.
        /// </summary>
        /// <param name="students">students.</param>
        /// <param name="currentStudentId">currentStudentId.</param>
        /// <param name="weekStart">weekStart.</param>
        /// <param name="yaClass">yaClass.</param>
        /// <param name="yaClassAuthUrl">yaClassAuthUrl.</param>
        /// <param name="newDiskToken">newDiskToken.</param>
        /// <param name="newDiskWasRequest">newDiskWasRequest.</param>
        /// <param name="ttsuRl">ttsuRl.</param>
        /// <param name="externalUrl">externalUrl.</param>
        /// <param name="weight">weight.</param>
        /// <param name="maxMark">maxMark.</param>
        /// <param name="withLaAssigns">withLaAssigns.</param>
        public StudentDiaryInit(List<StudentDiaryInitStudents> students = default(List<StudentDiaryInitStudents>), int? currentStudentId = default(int?), DateTime? weekStart = default(DateTime?), bool? yaClass = default(bool?), string yaClassAuthUrl = default(string), string newDiskToken = default(string), bool? newDiskWasRequest = default(bool?), string ttsuRl = default(string), string externalUrl = default(string), bool? weight = default(bool?), int? maxMark = default(int?), bool? withLaAssigns = default(bool?))
        {
            this.Students = students;
            this.CurrentStudentId = currentStudentId;
            this.WeekStart = weekStart;
            this.YaClass = yaClass;
            this.YaClassAuthUrl = yaClassAuthUrl;
            this.NewDiskToken = newDiskToken;
            this.NewDiskWasRequest = newDiskWasRequest;
            this.TtsuRl = ttsuRl;
            this.ExternalUrl = externalUrl;
            this.Weight = weight;
            this.MaxMark = maxMark;
            this.WithLaAssigns = withLaAssigns;
        }
        
        /// <summary>
        /// Gets or Sets Students
        /// </summary>
        [DataMember(Name="students", EmitDefaultValue=false)]
        public List<StudentDiaryInitStudents> Students { get; set; }

        /// <summary>
        /// Gets or Sets CurrentStudentId
        /// </summary>
        [DataMember(Name="currentStudentId", EmitDefaultValue=false)]
        public int? CurrentStudentId { get; set; }

        /// <summary>
        /// Gets or Sets WeekStart
        /// </summary>
        [DataMember(Name="weekStart", EmitDefaultValue=false)]
        [JsonConverter(typeof(SwaggerDateConverter))]
        public DateTime? WeekStart { get; set; }

        /// <summary>
        /// Gets or Sets YaClass
        /// </summary>
        [DataMember(Name="yaClass", EmitDefaultValue=false)]
        public bool? YaClass { get; set; }

        /// <summary>
        /// Gets or Sets YaClassAuthUrl
        /// </summary>
        [DataMember(Name="yaClassAuthUrl", EmitDefaultValue=false)]
        public string YaClassAuthUrl { get; set; }

        /// <summary>
        /// Gets or Sets NewDiskToken
        /// </summary>
        [DataMember(Name="newDiskToken", EmitDefaultValue=false)]
        public string NewDiskToken { get; set; }

        /// <summary>
        /// Gets or Sets NewDiskWasRequest
        /// </summary>
        [DataMember(Name="newDiskWasRequest", EmitDefaultValue=false)]
        public bool? NewDiskWasRequest { get; set; }

        /// <summary>
        /// Gets or Sets TtsuRl
        /// </summary>
        [DataMember(Name="ttsuRl", EmitDefaultValue=false)]
        public string TtsuRl { get; set; }

        /// <summary>
        /// Gets or Sets ExternalUrl
        /// </summary>
        [DataMember(Name="externalUrl", EmitDefaultValue=false)]
        public string ExternalUrl { get; set; }

        /// <summary>
        /// Gets or Sets Weight
        /// </summary>
        [DataMember(Name="weight", EmitDefaultValue=false)]
        public bool? Weight { get; set; }

        /// <summary>
        /// Gets or Sets MaxMark
        /// </summary>
        [DataMember(Name="maxMark", EmitDefaultValue=false)]
        public int? MaxMark { get; set; }

        /// <summary>
        /// Gets or Sets WithLaAssigns
        /// </summary>
        [DataMember(Name="withLaAssigns", EmitDefaultValue=false)]
        public bool? WithLaAssigns { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class StudentDiaryInit {\n");
            sb.Append("  Students: ").Append(Students).Append("\n");
            sb.Append("  CurrentStudentId: ").Append(CurrentStudentId).Append("\n");
            sb.Append("  WeekStart: ").Append(WeekStart).Append("\n");
            sb.Append("  YaClass: ").Append(YaClass).Append("\n");
            sb.Append("  YaClassAuthUrl: ").Append(YaClassAuthUrl).Append("\n");
            sb.Append("  NewDiskToken: ").Append(NewDiskToken).Append("\n");
            sb.Append("  NewDiskWasRequest: ").Append(NewDiskWasRequest).Append("\n");
            sb.Append("  TtsuRl: ").Append(TtsuRl).Append("\n");
            sb.Append("  ExternalUrl: ").Append(ExternalUrl).Append("\n");
            sb.Append("  Weight: ").Append(Weight).Append("\n");
            sb.Append("  MaxMark: ").Append(MaxMark).Append("\n");
            sb.Append("  WithLaAssigns: ").Append(WithLaAssigns).Append("\n");
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
            return this.Equals(input as StudentDiaryInit);
        }

        /// <summary>
        /// Returns true if StudentDiaryInit instances are equal
        /// </summary>
        /// <param name="input">Instance of StudentDiaryInit to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(StudentDiaryInit input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Students == input.Students ||
                    this.Students != null &&
                    input.Students != null &&
                    this.Students.SequenceEqual(input.Students)
                ) && 
                (
                    this.CurrentStudentId == input.CurrentStudentId ||
                    (this.CurrentStudentId != null &&
                    this.CurrentStudentId.Equals(input.CurrentStudentId))
                ) && 
                (
                    this.WeekStart == input.WeekStart ||
                    (this.WeekStart != null &&
                    this.WeekStart.Equals(input.WeekStart))
                ) && 
                (
                    this.YaClass == input.YaClass ||
                    (this.YaClass != null &&
                    this.YaClass.Equals(input.YaClass))
                ) && 
                (
                    this.YaClassAuthUrl == input.YaClassAuthUrl ||
                    (this.YaClassAuthUrl != null &&
                    this.YaClassAuthUrl.Equals(input.YaClassAuthUrl))
                ) && 
                (
                    this.NewDiskToken == input.NewDiskToken ||
                    (this.NewDiskToken != null &&
                    this.NewDiskToken.Equals(input.NewDiskToken))
                ) && 
                (
                    this.NewDiskWasRequest == input.NewDiskWasRequest ||
                    (this.NewDiskWasRequest != null &&
                    this.NewDiskWasRequest.Equals(input.NewDiskWasRequest))
                ) && 
                (
                    this.TtsuRl == input.TtsuRl ||
                    (this.TtsuRl != null &&
                    this.TtsuRl.Equals(input.TtsuRl))
                ) && 
                (
                    this.ExternalUrl == input.ExternalUrl ||
                    (this.ExternalUrl != null &&
                    this.ExternalUrl.Equals(input.ExternalUrl))
                ) && 
                (
                    this.Weight == input.Weight ||
                    (this.Weight != null &&
                    this.Weight.Equals(input.Weight))
                ) && 
                (
                    this.MaxMark == input.MaxMark ||
                    (this.MaxMark != null &&
                    this.MaxMark.Equals(input.MaxMark))
                ) && 
                (
                    this.WithLaAssigns == input.WithLaAssigns ||
                    (this.WithLaAssigns != null &&
                    this.WithLaAssigns.Equals(input.WithLaAssigns))
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
                if (this.Students != null)
                    hashCode = hashCode * 59 + this.Students.GetHashCode();
                if (this.CurrentStudentId != null)
                    hashCode = hashCode * 59 + this.CurrentStudentId.GetHashCode();
                if (this.WeekStart != null)
                    hashCode = hashCode * 59 + this.WeekStart.GetHashCode();
                if (this.YaClass != null)
                    hashCode = hashCode * 59 + this.YaClass.GetHashCode();
                if (this.YaClassAuthUrl != null)
                    hashCode = hashCode * 59 + this.YaClassAuthUrl.GetHashCode();
                if (this.NewDiskToken != null)
                    hashCode = hashCode * 59 + this.NewDiskToken.GetHashCode();
                if (this.NewDiskWasRequest != null)
                    hashCode = hashCode * 59 + this.NewDiskWasRequest.GetHashCode();
                if (this.TtsuRl != null)
                    hashCode = hashCode * 59 + this.TtsuRl.GetHashCode();
                if (this.ExternalUrl != null)
                    hashCode = hashCode * 59 + this.ExternalUrl.GetHashCode();
                if (this.Weight != null)
                    hashCode = hashCode * 59 + this.Weight.GetHashCode();
                if (this.MaxMark != null)
                    hashCode = hashCode * 59 + this.MaxMark.GetHashCode();
                if (this.WithLaAssigns != null)
                    hashCode = hashCode * 59 + this.WithLaAssigns.GetHashCode();
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