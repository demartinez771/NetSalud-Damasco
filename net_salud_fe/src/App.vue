<script>

</script>

<template>
  <div id="app">
    <div id="header">
      <img src="./assets/Logo.png" alt="" width="70" height="70">  
      <div id="slogan">
        <h1>NetSalud</h1>
        <h2>La salud a tus manos</h2>
      </div>
      
        <nav>
            <button v-if="is_auth" v-on:click="loadHome" > Inicio </button>
            <button v-if="is_auth" v-on:click="loadPatientRecord"> RegistroPaciente </button>
            <button v-if="is_auth" v-on:click="loaddoctorRecord"> RegistroMedico </button>
            <button v-if="is_auth" v-on:click="loadFamilyRecord"> RegistroFamiliar </button>
            <button v-if="is_auth" v-on:click="loadPatientConsult"> ConsultarPaciente </button>
            <button v-if="is_auth" v-on:click="logOut"> Cerrar Sesión </button>
        </nav>
    </div>
  </div>
</template>

<style>
#app {
  font-family: kanit;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2E2D4D;
  line-height: 0.3;
}
h2{
  font-size: 20px;
}
#header {
  flex-direction: row !important;
  display: flex !important;
}
#slogan{
  margin-left: 10px;
  background-color: #42b983;
}
nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
