#ifdef GL_ES
precision mediump float;
#endif

/* a variável “resolution” vem da aplicação e contem a
resolução da viewport */

uniform vec2 u_resolution;

void main() {
/* a variável gl_FragCoord armazena as coordenadas  do fragmento na tela */
vec2 st = gl_FragCoord.xy/u_resolution;
gl_FragColor = vec4(st.x,st.y,0.0,1.0);
}
