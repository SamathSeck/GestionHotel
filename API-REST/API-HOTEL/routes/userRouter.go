package routes

import (
	controller "golang-GESTION-Hotel/controllers"

	"github.com/gin-gonic/gin"
)

func UserRoutes(incomingRoutes *gin.Engine) {
	incomingRoutes.GET("/users", controller.GetUser()) //renvoie tous les utilisateurs de l'application.

	incomingRoutes.GET("/users/:user_id", controller.GetUser()) //renvoie les détails de l'utilisateur avec l'ID spécifié

	incomingRoutes.POST("/users/signup", controller.SignUp()) //un nouvel utilisateur de s'inscrire

	incomingRoutes.POST("/users/login", controller.Login()) //n utilisateur existant de se connecter à l'application
}
