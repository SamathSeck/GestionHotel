package middleware

import (
	"fmt"
	helper "golang-GESTION-Hotel/helpers"
	"net/http"

	"github.com/gin-gonic/gin"
)

func Authentication() gin.HandlerFunc { //authentification
	return func(c *gin.Context) {
		clientToken := c.Request.Header.Get("token")
		if clientToken == "" {
			c.JSON(http.StatusInternalServerError, gin.H{"error": fmt.Sprintf("No authorization header provides")})
			c.Abort()
			return
		}

		claims, err := helper.ValidateToken(clientToken)
		if err != "" {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err})
			c.Abort()
			return
		}

		c.Set("email", claims.Email)
		c.Set("FirstName", claims.FirstName)
		c.Set("LastNAme", claims.LastName)
		c.Set("uid", claims.Uid)

		c.Next()
	}
}

//vérification la validité du jeton d'authentification et stocke les informations de l'utilisateur
