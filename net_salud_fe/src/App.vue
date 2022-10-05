<script>
export default {

  data: function () {
    return {
      is_auth: false
    }
  },
  methods: {
    loadHome: function () {
      this.$router.push({ name: "home" });
    },
    loadPatientRecord: function () {
      this.$router.push({ name: "patientRecord" });
    },
    loadDoctorRecord: function () {
      this.$router.push({ name: "doctorRecord" });
    },
    loadFamilyRecord: function () {
      this.$router.push({ name: "familyRecord" });
    },
    loadPatientConsult: function () {
      this.$router.push({ name: "patientConsult" });
    },
    loadUser: function () {
      this.$router.push({ name: "user" });
    },
    loadLogIn: function () {
      this.$router.push({ name: "logIn" });
    },
  },

}
</script>

<template>
  <div class="general-div">
    <div class="header column">
      <div class="row sub-header1">
        <div class="row div-logo">
          <img src="./assets/Logo.svg" alt="" width="70" height="70" />
          <div class="slogan column">
            <h1>NetSalud</h1>
            <h2>La salud a tus manos</h2>
          </div>
        </div>
        <div>
          <h2 class="perfil">Bienvenido!</h2>
        </div>
        <div>
          <!--<h2 class="c_s">Cerrar Sesión</h2>-->
        </div>
      </div>
      <nav class="row">
        <!--<button v-on:click="loadHome">Inicio</button>-->
        <!--<button v-if="loadPatientRecord">Registro Paciente</button>-->
        <!--<button v-if="loadDoctorRecord">Registro Medico</button>-->
        <!--<button v-if="loadFamilyRecord">Registro Familiar</button>-->
        <!--<button v-if="loadPatientConsult">Consultar Paciente</button>-->
        <button v-on:click="loadUser">Registro de usuario</button>
        <button v-on:click="loadLogIn">Login</button>
      </nav>
    </div>
    <div class="main-component">
      <router-view></router-view>
    </div>
    <footer>Copyright 2022 by Damasco. All Rights Reserved.</footer>
  </div>
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;1,100;1,200;1,300;1,400;1,500&display=swap");

.row {
  display: flex;
  flex-direction: row;
}

.column {
  display: flex;
  flex-direction: column;
}

h2 {
  font-size: 30px;
  font-family: "Kanit";
  font-weight: 400;
}

.general-div {
  width: 100%;
  margin: 0%;
  overflow: hidden;
}

.perfil {
  font-style: oblique;
  justify-content: center;
  color: #db5461;
  font-size: 20px;
  height: 70px;
}

.c_s {
  color: #8aa29e;
  display: flex;
  align-items: right;
  align-items: flex-end;
  text-decoration-line: underline;
  margin-left: 130px;
}

.c_s:hover {
  color: #db5461;
  pointer-events: auto;
}

.header {
  width: 100vw;
  align-items: center;
}

.sub-header1 {
  width: 90%;
  height: 90px;
  padding: 0px 2.5%;
  justify-content: space-between;
  align-items: center;
}

.div-logo {
  flex-direction: row !important;
  display: flex !important;
}

.slogan {
  margin-left: 10px;
  font-family: "Kanit";
  display: flex;
  color: #2e2d4d;
  line-height: 0%;
  justify-content: center;
}

.main-component {}

nav {
  width: 95%;
  justify-content: right;
  padding-left: 10px;
  padding-right: 10px;
}

nav button {
  width: 15%;
  color: #e3f2fd;
  background: #8aa29e;
  border: 1px solid;
  border-radius: 15px;
  padding: 4px 20px;
  font-size: 20px;
  font-family: "Kanit";
}

nav button:hover {
  color: #e3f2fd;
  background: #db5461;
  border: 1px solid #e5e7e9;
}

footer {
  background-color: #8aa29e;
  position: absolute;
  align-items: center;
  justify-content: center;
  display: flex;
  width: 95%;
  bottom: 0;
  height: 60px;
  color: #e3f2fd;
  left: 0%;
  padding: 0px 2.5%;
}
</style>
