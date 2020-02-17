<template>
  <v-app>
    <v-content>
      <div class="stage">
        <div class="layer"></div>
        <div class="layer"></div>
        <div class="layer"></div>
        <div class="layer"></div>
        <div class="layer"></div>
        <div class="layer"></div>
        <div class="layer"></div>
        <div class="layer"></div>
        <div class="layer"></div>
        <div class="layer"></div>
        <div class="layer"></div>
        <div class="layer"></div>
        <div class="layer"></div>
        <div class="layer"></div>
        <div class="layer"></div>
        <div class="layer"></div>
        <div class="layer"></div>
        <div class="layer"></div>
        <div class="layer"></div>
        <div class="layer"></div>
      </div>
      <TextBox />
    </v-content>
  </v-app>
</template>

<script>
import TextBox from "./components/TextBox";

export default {
  name: "App",

  components: {
    TextBox
  },

  data: () => ({
    //
  })
};
</script>

<style lang="scss">
@import url("//fonts.googleapis.com/css?family=Pacifico&text=Pure");
@import url("//fonts.googleapis.com/css?family=Roboto:700&text=css");
@import url("//fonts.googleapis.com/css?family=Kaushan+Script&text=!");

body {
  min-height: 450px;
  height: 100vh;
  margin: 0;
  background: radial-gradient(
    circle,
    darken(dodgerblue, 10%),
    #1f4f96,
    #1b2949,
    #000
  );
}

.stage {
  margin-top: 60px;
  margin-bottom: 150px;
  transform: scale(0.5);
  perspective: 9999px;
  transform-style: preserve-3d;
}

.layer {
  width: 100%;
  height: 100%;
  position: absolute;
  transform-style: preserve-3d;
  animation: ಠ_ಠ 5s infinite alternate ease-in-out -7.5s;
  animation-fill-mode: forwards;
  transform: rotateY(20deg) rotateX(13deg) translateZ(0);
}

.layer:after {
  font: 150px/0.65 "Pacifico", "Kaushan Script", Futura, "Roboto",
    "Trebuchet MS", Helvetica, sans-serif;
  content: "Magic Text";
  white-space: pre;
  text-align: center;
  height: 100%;
  width: 100%;
  position: absolute;
  top: 0px;
  color: darken(#fff, 4%);
  letter-spacing: -2px;
  text-shadow: 4px 0 10px hsla(0, 0%, 0%, 0.13);
}

$i: 1;
$NUM_LAYERS: 20;
@for $i from 1 through $NUM_LAYERS {
  .layer:nth-child(#{$i}):after {
    transform: translateZ(($i - 1) * -1.5px);
  }
}

.layer:nth-child(n + #{round($NUM_LAYERS/2)}):after {
  -webkit-text-stroke: 3px hsla(0, 0%, 0%, 0.25);
}

.layer:nth-child(n + #{round($NUM_LAYERS/2 + 1)}):after {
  -webkit-text-stroke: 15px dodgerblue;
  text-shadow: 6px 0 6px darken(dodgerblue, 35%),
    5px 5px 5px darken(dodgerblue, 40%), 0 6px 6px darken(dodgerblue, 35%);
}

.layer:nth-child(n + #{round($NUM_LAYERS/2 + 2)}):after {
  -webkit-text-stroke: 15px darken(dodgerblue, 10%);
}

.layer:last-child:after {
  -webkit-text-stroke: 17px hsla(0, 0%, 0%, 0.1);
}

.layer:first-child:after {
  color: #fff;
  text-shadow: none;
}

@keyframes ಠ_ಠ {
  100% {
    transform: rotateY(-20deg) rotateX(-13deg);
  }
}

h1 {
  margin-top: 50px;
  color: white;
  text-align: center;
}
#app {
  background: repeating-linear-gradient(
      135deg,
      hsla(111, 77%, 90%, 0.06) 0px,
      hsla(111, 77%, 90%, 0.06) 1px,
      transparent 1px,
      transparent 11px,
      hsla(111, 77%, 90%, 0.06) 11px,
      hsla(111, 77%, 90%, 0.06) 12px,
      transparent 12px,
      transparent 32px
    ),
    repeating-linear-gradient(
      45deg,
      hsla(111, 77%, 90%, 0.06) 0px,
      hsla(111, 77%, 90%, 0.06) 1px,
      transparent 1px,
      transparent 11px,
      hsla(111, 77%, 90%, 0.06) 11px,
      hsla(111, 77%, 90%, 0.06) 12px,
      transparent 12px,
      transparent 32px
    ),
    repeating-linear-gradient(
      135deg,
      hsla(111, 77%, 90%, 0.06) 0px,
      hsla(111, 77%, 90%, 0.06) 1px,
      transparent 1px,
      transparent 11px,
      hsla(111, 77%, 90%, 0.06) 11px,
      hsla(111, 77%, 90%, 0.06) 12px,
      transparent 12px,
      transparent 32px
    ),
    repeating-linear-gradient(
      45deg,
      hsla(111, 77%, 90%, 0.06) 0px,
      hsla(111, 77%, 90%, 0.06) 1px,
      transparent 1px,
      transparent 11px,
      hsla(111, 77%, 90%, 0.06) 11px,
      hsla(111, 77%, 90%, 0.06) 12px,
      transparent 12px,
      transparent 32px
    ),
    linear-gradient(90deg, hsl(230, 78%, 25%), hsl(230, 78%, 25%));
}
</style>
