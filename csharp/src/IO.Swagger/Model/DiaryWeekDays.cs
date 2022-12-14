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
    /// DiaryWeekDays
    /// </summary>
    [DataContract]
        public partial class DiaryWeekDays :  IEquatable<DiaryWeekDays>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DiaryWeekDays" /> class.
        /// </summary>
        /// <param name="date">date.</param>
        /// <param name="lessons">lessons.</param>
        public DiaryWeekDays(DateTime? date = default(DateTime?), List<DiaryLesson> lessons = default(List<DiaryLesson>))
        {
            this.Date = date;
            this.Lessons = lessons;
        }
        
        /// <summary>
        /// Gets or Sets Date
        /// </summary>
        [DataMember(Name="date", EmitDefaultValue=false)]
        [JsonConverter(typeof(SwaggerDateConverter))]
        public DateTime? Date { get; set; }

        /// <summary>
        /// Gets or Sets Lessons
        /// </summary>
        [DataMember(Name="lessons", EmitDefaultValue=false)]
        public List<DiaryLesson> Lessons { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DiaryWeekDays {\n");
            sb.Append("  Date: ").Append(Date).Append("\n");
            sb.Append("  Lessons: ").Append(Lessons).Append("\n");
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
            return this.Equals(input as DiaryWeekDays);
        }

        /// <summary>
        /// Returns true if DiaryWeekDays instances are equal
        /// </summary>
        /// <param name="input">Instance of DiaryWeekDays to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DiaryWeekDays input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Date == input.Date ||
                    (this.Date != null &&
                    this.Date.Equals(input.Date))
                ) && 
                (
                    this.Lessons == input.Lessons ||
                    this.Lessons != null &&
                    input.Lessons != null &&
                    this.Lessons.SequenceEqual(input.Lessons)
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
                if (this.Date != null)
                    hashCode = hashCode * 59 + this.Date.GetHashCode();
                if (this.Lessons != null)
                    hashCode = hashCode * 59 + this.Lessons.GetHashCode();
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
