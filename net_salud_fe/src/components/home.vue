<script></script>

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
