<script>
  import jwt_decode from 'jwt-decode';
import axios from 'axios';

export default {
    name: "home",

    data: function () {
        return {
        username: "",
        password: "",
        perfil: "",
        nombre: "",
        apellido: "",
        celular: "",
        genero: "",
        }
    },

    methods: {
        getData: async function () {
            if (localStorage.getItem("token_access") === null || localStorage.getItem("token_refresh") === null) {
                this.$emit('logOut');
                return;
            }

            await this.verifyToken();
            let token = localStorage.getItem("token_access");
            //let username = jwt_decode(token).username.toString();
            axios.get(`https://netsalud-be-123.herokuapp.com/usuario/`,

                { headers: { 'Authorization': `Bearer ${token}` } })
                .then((result) => {
                    this.username = result.data.username;
                    this.password = result.data.password;
                    this.perfil = result.data.perfil;
                    this.nombre = result.data.nombre;
                    this.apellido = result.data.apellido;
                    this.celular = result.data.celular;
                    this.genero = result.data.genero;
                    this.loaded = true;
                })

                .catch((error) => {
                    this.$emit('logOut');
                    console.log(error);
                });
        },

        verifyToken: function () {
            return axios.post("https://netsalud-be-123.herokuapp.com/refresh/", { refresh: localStorage.getItem("token_refresh") }, { headers: {} })
                .then((result) => {
                    localStorage.setItem("token_access", result.data.access);
                })
                .catch(() => {
                    this.$emit('logOut');
                });
        }
    },

    created: async function () {
        this.getData();
    },
}
</script>

<template>
  <div class="containerhome">
    <div class="prueba">
      <div class="Auxiliar"></div>
    </div>
    <div class="texto" style="color: #2e2d4d">
      Bienvenido al perfil de auxiliar
    </div>
  </div>
</template>

<style>
.containerhome {
  display: flex;
  align-items: center;
  justify-content: center;
}

.Auxiliar {
  position:absolute;
  background-image: url(../assets/Logo.png);
  background-repeat: no-repeat;
  background-size: 70%;
  opacity: 0.2;
  z-index: 1;
  margin-top: 100px;
  padding: 0%;
  width: 648px;
  height: 648px;
}
.texto {
  position: absolute;
  bottom: 100px;
  z-index: 10;
  font-family: "Kanit";
  font-style: normal;
  font-weight: 400;
  font-size: 60px;
  line-height: 90px;
  color: #2e2d4d;
}
</style>
