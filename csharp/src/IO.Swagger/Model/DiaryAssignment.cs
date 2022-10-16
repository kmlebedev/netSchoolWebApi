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
    /// DiaryAssignment
    /// </summary>
    [DataContract]
        public partial class DiaryAssignment :  IEquatable<DiaryAssignment>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DiaryAssignment" /> class.
        /// </summary>
        /// <param name="mark">mark.</param>
        /// <param name="attachments">attachments.</param>
        /// <param name="id">id.</param>
        /// <param name="typeId">typeId.</param>
        /// <param name="assignmentName">assignmentName.</param>
        /// <param name="weight">weight.</param>
        /// <param name="dueDate">dueDate.</param>
        /// <param name="classMeetingId">classMeetingId.</param>
        /// <param name="existsTestPlan">existsTestPlan.</param>
        public DiaryAssignment(Mark mark = default(Mark), List<Attachment> attachments = default(List<Attachment>), int? id = default(int?), int? typeId = default(int?), string assignmentName = default(string), int? weight = default(int?), DateTime? dueDate = default(DateTime?), int? classMeetingId = default(int?), bool? existsTestPlan = default(bool?))
        {
            this.Mark = mark;
            this.Attachments = attachments;
            this.Id = id;
            this.TypeId = typeId;
            this.AssignmentName = assignmentName;
            this.Weight = weight;
            this.DueDate = dueDate;
            this.ClassMeetingId = classMeetingId;
            this.ExistsTestPlan = existsTestPlan;
        }
        
        /// <summary>
        /// Gets or Sets Mark
        /// </summary>
        [DataMember(Name="mark", EmitDefaultValue=false)]
        public Mark Mark { get; set; }

        /// <summary>
        /// Gets or Sets Attachments
        /// </summary>
        [DataMember(Name="attachments", EmitDefaultValue=false)]
        public List<Attachment> Attachments { get; set; }

        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name="id", EmitDefaultValue=false)]
        public int? Id { get; set; }

        /// <summary>
        /// Gets or Sets TypeId
        /// </summary>
        [DataMember(Name="typeId", EmitDefaultValue=false)]
        public int? TypeId { get; set; }

        /// <summary>
        /// Gets or Sets AssignmentName
        /// </summary>
        [DataMember(Name="assignmentName", EmitDefaultValue=false)]
        public string AssignmentName { get; set; }

        /// <summary>
        /// Gets or Sets Weight
        /// </summary>
        [DataMember(Name="weight", EmitDefaultValue=false)]
        public int? Weight { get; set; }

        /// <summary>
        /// Gets or Sets DueDate
        /// </summary>
        [DataMember(Name="dueDate", EmitDefaultValue=false)]
        [JsonConverter(typeof(SwaggerDateConverter))]
        public DateTime? DueDate { get; set; }

        /// <summary>
        /// Gets or Sets ClassMeetingId
        /// </summary>
        [DataMember(Name="classMeetingId", EmitDefaultValue=false)]
        public int? ClassMeetingId { get; set; }

        /// <summary>
        /// Gets or Sets ExistsTestPlan
        /// </summary>
        [DataMember(Name="existsTestPlan", EmitDefaultValue=false)]
        public bool? ExistsTestPlan { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DiaryAssignment {\n");
            sb.Append("  Mark: ").Append(Mark).Append("\n");
            sb.Append("  Attachments: ").Append(Attachments).Append("\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  TypeId: ").Append(TypeId).Append("\n");
            sb.Append("  AssignmentName: ").Append(AssignmentName).Append("\n");
            sb.Append("  Weight: ").Append(Weight).Append("\n");
            sb.Append("  DueDate: ").Append(DueDate).Append("\n");
            sb.Append("  ClassMeetingId: ").Append(ClassMeetingId).Append("\n");
            sb.Append("  ExistsTestPlan: ").Append(ExistsTestPlan).Append("\n");
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
            return this.Equals(input as DiaryAssignment);
        }

        /// <summary>
        /// Returns true if DiaryAssignment instances are equal
        /// </summary>
        /// <param name="input">Instance of DiaryAssignment to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DiaryAssignment input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Mark == input.Mark ||
                    (this.Mark != null &&
                    this.Mark.Equals(input.Mark))
                ) && 
                (
                    this.Attachments == input.Attachments ||
                    this.Attachments != null &&
                    input.Attachments != null &&
                    this.Attachments.SequenceEqual(input.Attachments)
                ) && 
                (
                    this.Id == input.Id ||
                    (this.Id != null &&
                    this.Id.Equals(input.Id))
                ) && 
                (
                    this.TypeId == input.TypeId ||
                    (this.TypeId != null &&
                    this.TypeId.Equals(input.TypeId))
                ) && 
                (
                    this.AssignmentName == input.AssignmentName ||
                    (this.AssignmentName != null &&
                    this.AssignmentName.Equals(input.AssignmentName))
                ) && 
                (
                    this.Weight == input.Weight ||
                    (this.Weight != null &&
                    this.Weight.Equals(input.Weight))
                ) && 
                (
                    this.DueDate == input.DueDate ||
                    (this.DueDate != null &&
                    this.DueDate.Equals(input.DueDate))
                ) && 
                (
                    this.ClassMeetingId == input.ClassMeetingId ||
                    (this.ClassMeetingId != null &&
                    this.ClassMeetingId.Equals(input.ClassMeetingId))
                ) && 
                (
                    this.ExistsTestPlan == input.ExistsTestPlan ||
                    (this.ExistsTestPlan != null &&
                    this.ExistsTestPlan.Equals(input.ExistsTestPlan))
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
                if (this.Mark != null)
                    hashCode = hashCode * 59 + this.Mark.GetHashCode();
                if (this.Attachments != null)
                    hashCode = hashCode * 59 + this.Attachments.GetHashCode();
                if (this.Id != null)
                    hashCode = hashCode * 59 + this.Id.GetHashCode();
                if (this.TypeId != null)
                    hashCode = hashCode * 59 + this.TypeId.GetHashCode();
                if (this.AssignmentName != null)
                    hashCode = hashCode * 59 + this.AssignmentName.GetHashCode();
                if (this.Weight != null)
                    hashCode = hashCode * 59 + this.Weight.GetHashCode();
                if (this.DueDate != null)
                    hashCode = hashCode * 59 + this.DueDate.GetHashCode();
                if (this.ClassMeetingId != null)
                    hashCode = hashCode * 59 + this.ClassMeetingId.GetHashCode();
                if (this.ExistsTestPlan != null)
                    hashCode = hashCode * 59 + this.ExistsTestPlan.GetHashCode();
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
