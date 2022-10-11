/**
 * NetSchool
 * The API for the NetSchool irTech project
 *
 * OpenAPI spec version: 4.30.43656
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */
package io.swagger.client.api

import java.text.SimpleDateFormat

import io.swagger.client.model.Diary
import io.swagger.client.model.date
import io.swagger.client.model.studentDiaryInit
import io.swagger.client.{ApiInvoker, ApiException}

import com.sun.jersey.multipart.FormDataMultiPart
import com.sun.jersey.multipart.file.FileDataBodyPart

import javax.ws.rs.core.MediaType

import java.io.File
import java.util.Date
import java.util.TimeZone

import scala.collection.mutable.HashMap

import com.wordnik.swagger.client._
import scala.concurrent.Future
import collection.mutable

import java.net.URI

import com.wordnik.swagger.client.ClientResponseReaders.Json4sFormatsReader._
import com.wordnik.swagger.client.RequestWriters.Json4sFormatsWriter._

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent._
import scala.concurrent.duration._
import scala.util.{Failure, Success, Try}

import org.json4s._

class StudentApi(
  val defBasePath: String = "https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/4.30.43656",
  defApiInvoker: ApiInvoker = ApiInvoker
) {
  private lazy val dateTimeFormatter = {
    val formatter = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSSZ")
    formatter.setTimeZone(TimeZone.getTimeZone("UTC"))
    formatter
  }
  private val dateFormatter = {
    val formatter = new SimpleDateFormat("yyyy-MM-dd")
    formatter.setTimeZone(TimeZone.getTimeZone("UTC"))
    formatter
  }
  implicit val formats = new org.json4s.DefaultFormats {
    override def dateFormatter = dateTimeFormatter
  }
  implicit val stringReader: ClientResponseReader[String] = ClientResponseReaders.StringReader
  implicit val unitReader: ClientResponseReader[Unit] = ClientResponseReaders.UnitReader
  implicit val jvalueReader: ClientResponseReader[JValue] = ClientResponseReaders.JValueReader
  implicit val jsonReader: ClientResponseReader[Nothing] = JsonFormatsReader
  implicit val stringWriter: RequestWriter[String] = RequestWriters.StringWriter
  implicit val jsonWriter: RequestWriter[Nothing] = JsonFormatsWriter

  var basePath: String = defBasePath
  var apiInvoker: ApiInvoker = defApiInvoker

  def addHeader(key: String, value: String): mutable.HashMap[String, String] = {
    apiInvoker.defaultHeaders += key -> value
  }

  val config: SwaggerConfig = SwaggerConfig.forUrl(new URI(defBasePath))
  val client = new RestClient(config)
  val helper = new StudentApiAsyncHelper(client, config)

  /**
   * 
   * returns all assignments
   *
   * @param studentId  
   * @param weekStart  (optional)
   * @param weekEnd  (optional)
   * @param withLaAssigns  (optional)
   * @param withPastMandatory  (optional)
   * @param yearId  (optional)
   * @return Diary
   */
  def studentDiary(studentId: Integer, weekStart: Option[date] = None, weekEnd: Option[date] = None, withLaAssigns: Option[Boolean] = None, withPastMandatory: Option[Boolean] = None, yearId: Option[Integer] = None): Option[Diary] = {
    val await = Try(Await.result(studentDiaryAsync(studentId, weekStart, weekEnd, withLaAssigns, withPastMandatory, yearId), Duration.Inf))
    await match {
      case Success(i) => Some(await.get)
      case Failure(t) => None
    }
  }

  /**
   *  asynchronously
   * returns all assignments
   *
   * @param studentId  
   * @param weekStart  (optional)
   * @param weekEnd  (optional)
   * @param withLaAssigns  (optional)
   * @param withPastMandatory  (optional)
   * @param yearId  (optional)
   * @return Future(Diary)
   */
  def studentDiaryAsync(studentId: Integer, weekStart: Option[date] = None, weekEnd: Option[date] = None, withLaAssigns: Option[Boolean] = None, withPastMandatory: Option[Boolean] = None, yearId: Option[Integer] = None): Future[Diary] = {
      helper.studentDiary(studentId, weekStart, weekEnd, withLaAssigns, withPastMandatory, yearId)
  }

  /**
   * 
   * returns strudent diary init data
   *
   * @return studentDiaryInit
   */
  def studentDiaryInit(): Option[studentDiaryInit] = {
    val await = Try(Await.result(studentDiaryInitAsync(), Duration.Inf))
    await match {
      case Success(i) => Some(await.get)
      case Failure(t) => None
    }
  }

  /**
   *  asynchronously
   * returns strudent diary init data
   *
   * @return Future(studentDiaryInit)
   */
  def studentDiaryInitAsync(): Future[studentDiaryInit] = {
      helper.studentDiaryInit()
  }

}

class StudentApiAsyncHelper(client: TransportClient, config: SwaggerConfig) extends ApiClient(client, config) {

  def studentDiary(studentId: Integer,
    weekStart: Option[date] = None,
    weekEnd: Option[date] = None,
    withLaAssigns: Option[Boolean] = None,
    withPastMandatory: Option[Boolean] = None,
    yearId: Option[Integer] = None
    )(implicit reader: ClientResponseReader[Diary]): Future[Diary] = {
    // create path and map variables
    val path = (addFmt("/student/diary"))

    // query params
    val queryParams = new mutable.HashMap[String, String]
    val headerParams = new mutable.HashMap[String, String]

    queryParams += "studentId" -> studentId.toString
    weekStart match {
      case Some(param) => queryParams += "weekStart" -> param.toString
      case _ => queryParams
    }
    weekEnd match {
      case Some(param) => queryParams += "weekEnd" -> param.toString
      case _ => queryParams
    }
    withLaAssigns match {
      case Some(param) => queryParams += "withLaAssigns" -> param.toString
      case _ => queryParams
    }
    withPastMandatory match {
      case Some(param) => queryParams += "withPastMandatory" -> param.toString
      case _ => queryParams
    }
    yearId match {
      case Some(param) => queryParams += "yearId" -> param.toString
      case _ => queryParams
    }

    val resFuture = client.submit("GET", path, queryParams.toMap, headerParams.toMap, "")
    resFuture flatMap { resp =>
      process(reader.read(resp))
    }
  }

  def studentDiaryInit()(implicit reader: ClientResponseReader[studentDiaryInit]): Future[studentDiaryInit] = {
    // create path and map variables
    val path = (addFmt("/student/diary/init"))

    // query params
    val queryParams = new mutable.HashMap[String, String]
    val headerParams = new mutable.HashMap[String, String]


    val resFuture = client.submit("GET", path, queryParams.toMap, headerParams.toMap, "")
    resFuture flatMap { resp =>
      process(reader.read(resp))
    }
  }


}