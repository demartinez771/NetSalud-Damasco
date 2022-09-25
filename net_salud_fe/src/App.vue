<script></script>

<template>
  <div id="app">
    <div id="header">
      <div id="div-logo">
        <img
          src="./assets/Logo1.svg"
          alt=""
          width="70"
          height="70"
          style="filter: opacity(0.7) drop-shadow(0 0 0 #2e2d4d)"
        />
        <div id="slogan">
          <h1>NetSalud</h1>
          <h2>La salud a tus manos</h2>
        </div>
      </div>
      <div><h2 id="perfil">Perfil Auxiliar</h2></div>
      <div><h2 id="c_s">Cerrar Sesión</h2></div>
      <nav>
        <button v-if="is_auth" v-on:click="loadHome">Inicio</button>
        <button v-if="is_auth" v-on:click="loadPatientRecord">
          RegistroPaciente
        </button>
        <button v-if="is_auth" v-on:click="loaddoctorRecord">
          RegistroMedico
        </button>
        <button v-if="is_auth" v-on:click="loadFamilyRecord">
          RegistroFamiliar
        </button>
        <button v-if="is_auth" v-on:click="loadPatientConsult">
          ConsultarPaciente
        </button>
        <button v-if="is_auth" v-on:click="logOut">Cerrar Sesión</button>
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
  color: #2e2d4d;
  line-height: 0.3;
  padding: 10px;
}

h2 {
  font-size: 20px;
  font-family: "Kanit";
}
#perfil {
  width: 800px;
  height: 56px;
  font-style: normal;
  font-weight: 400;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  color: #db5461;
}
#c_s {
  color: #8aa29e;
  display: flex;
  height: 56px;
  align-items: center;
}

#header {
  flex-direction: row !important;
  display: flex !important;
  justify-content: space-between;
}
#div-logo {
  flex-direction: row !important;
  display: flex !important;
}
#slogan {
  margin-left: 10px;
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
