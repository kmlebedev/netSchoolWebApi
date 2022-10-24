/*
 * NetSchool
 *
 * The API for the NetSchool irTech project
 *
 * API version: 5.10.63221
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package swagger

type LoginData struct {
	ProductName string `json:"productName,omitempty"`
	Version string `json:"version,omitempty"`
	SchoolLogin bool `json:"schoolLogin,omitempty"`
	EmLogin bool `json:"emLogin,omitempty"`
	EsiaLogin bool `json:"esiaLogin,omitempty"`
	EsiaLoginPage string `json:"esiaLoginPage,omitempty"`
	EsiaMainAuth bool `json:"esiaMainAuth,omitempty"`
	EsiaButton bool `json:"esiaButton,omitempty"`
	SignatureLogin bool `json:"signatureLogin,omitempty"`
	CacheVer string `json:"cacheVer,omitempty"`
	WindowsAuth bool `json:"windowsAuth,omitempty"`
	EnableSms bool `json:"enableSms,omitempty"`
	EsaLogin bool `json:"esaLogin,omitempty"`
	EsaLoginPage string `json:"esaLoginPage,omitempty"`
}
