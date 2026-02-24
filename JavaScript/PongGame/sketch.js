let playerY, playerHeight, playerWidth;
let computerY, computerHeight, computerWidth;
let ballX, ballY, ballSpeedX, ballSpeedY, ballRadius;
let playerSpeed;
let gameWidth = 800, gameHeight = 500; // Campo de jogo maior
let errorMargin = 50; // Margem de erro do computador
let playerScore = 0; // Contador de pontos do jogador
let computerScore = 0; // Contador de pontos do computador
let maxBounceAngle = Math.PI / 4; // Ângulo máximo (45 graus)
let backgroundImage, ballImage, playerImage, computerImage;
let ballAngle = 0; // Ângulo de rotação da bola
const rotationSpeedFactor = 0.02; // Fator de rotação alterado
let bounceSound; // Variável para armazenar o som
let pointSound; // Som do ponto do jogador
let compSound; // Som do ponto do computador

function preload() {
  backgroundImage = loadImage('fundo.png');  // Carregar fundo
  ballImage = loadImage('bola.png');         // Carregar sprite da bola
  playerImage = loadImage('barra1.png');     // Carregar sprite da barra do jogador
  computerImage = loadImage('barra2.png');   // Carregar sprite da barra do computador
  bounceSound = loadSound('bounce.wav');     // Carregar som de colisão
  pointSound = loadSound('point.wav');       // Carregar som de ponto do jogador
  compSound = loadSound('comp.wav');         // Carregar som de ponto do computador
}

function setup() {
  createCanvas(gameWidth, gameHeight);
  
  // Configurações do jogador
  playerWidth = 10;
  playerHeight = 100;
  playerY = (height - playerHeight) / 2;
  playerSpeed = 5; // Velocidade do jogador e computador
  
  // Configurações do computador
  computerWidth = 10;
  computerHeight = 100;
  computerY = (height - computerHeight) / 2;
  
  // Configurações da bola
  ballRadius = 20; // Aumentado para 20
  resetBall(); // Inicia a bola no centro
}

function draw() {
  image(backgroundImage, 0, 0, width, height); // Desenha a imagem de fundo
  
  // Desenhar jogador e computador com as imagens
  image(playerImage, 10, playerY, playerWidth, playerHeight); // Sprite da barra do jogador
  image(computerImage, width - 20, computerY, computerWidth, computerHeight); // Sprite da barra do computador
  
  // Atualizar o ângulo da bola com base na sua velocidade
  ballAngle += (abs(ballSpeedX) + abs(ballSpeedY)) * rotationSpeedFactor; // Ajusta a rotação da bola
  push(); // Salva o estado atual do contexto
  translate(ballX, ballY); // Move o contexto para a posição da bola
  rotate(ballAngle); // Aplica a rotação
  image(ballImage, -ballRadius, -ballRadius, ballRadius * 2, ballRadius * 2); // Sprite da bola
  pop(); // Restaura o estado anterior do contexto
  
  // Atualizar posição do jogador com o mouse
  playerY = mouseY - playerHeight / 2; // Centraliza a raquete no mouse
  playerY = constrain(playerY, 0, height - playerHeight); // Limitar o movimento dentro da tela
  
  // Movimentar computador
  moveComputer();
  
  // Movimentar bola
  ballX += ballSpeedX;
  ballY += ballSpeedY;
  
  // Detectar colisão com bordas superiores e inferiores
  if (ballY < ballRadius || ballY > height - ballRadius) {
    ballSpeedY *= -1;
  }
  
  // Detectar colisão com o jogador
  if (ballX - ballRadius < 20 && ballY > playerY && ballY < playerY + playerHeight) {
    let relativeIntersectY = (ballY - (playerY + playerHeight / 2)); // Distância da bola ao centro da raquete
    let normalizedRelativeIntersectionY = relativeIntersectY / (playerHeight / 2); // Normaliza entre -1 e 1
    let bounceAngle = normalizedRelativeIntersectionY * maxBounceAngle; // Calcula o ângulo de colisão
    
    ballSpeedX = abs(ballSpeedX) * 1.1; // Mantém a bola indo para a direita e aumenta a velocidade
    ballSpeedY = ballSpeedX * tan(bounceAngle); // Define a velocidade vertical com base no ângulo de retorno
    ballX = 20 + ballRadius; // Evita bug de sobreposição
    bounceSound.play(); // Toca o som de colisão
  }
  
  // Detectar colisão com o computador
  if (ballX + ballRadius > width - 20 && ballY > computerY && ballY < computerY + computerHeight) {
    let relativeIntersectY = (ballY - (computerY + computerHeight / 2)); // Distância da bola ao centro da raquete
    let normalizedRelativeIntersectionY = relativeIntersectY / (computerHeight / 2); // Normaliza entre -1 e 1
    let bounceAngle = normalizedRelativeIntersectionY * maxBounceAngle; // Calcula o ângulo de colisão
    
    ballSpeedX = -abs(ballSpeedX) * 1.1; // Mantém a bola indo para a esquerda e aumenta a velocidade
    ballSpeedY = ballSpeedX * tan(bounceAngle); // Define a velocidade vertical com base no ângulo de retorno
    ballX = width - 20 - ballRadius; // Evita bug de sobreposição
    bounceSound.play(); // Toca o som de colisão
  }
  
  // Verificar se a bola saiu pela lateral (ponto)
  if (ballX - ballRadius < 0) {
    computerScore++; // O computador ganhou um ponto
    compSound.play(); // Toca o som de ponto do computador
    resetBall("computer"); // Reinicia a bola na direção do computador
  } else if (ballX + ballRadius > width) {
    playerScore++; // O jogador ganhou um ponto
    pointSound.play(); // Toca o som de ponto do jogador
    resetBall("player"); // Reinicia a bola na direção do jogador
  }
}

function resetBall(winner) {
  ballX = width / 2;
  ballY = height / 2;

  // A direção da bola depende de quem ganhou
  if (winner === "computer") {
    ballSpeedX = 6; // Começa a ir para a direita
  } else {
    ballSpeedX = -6; // Começa a ir para a esquerda
  }
  
  ballSpeedY = random([-4, 4]); // Aumenta a velocidade vertical da bola
}

function moveComputer() {
  // O computador segue a bola, mas com um erro intencional para facilitar para o jogador
  let targetY = ballY - computerHeight / 2;
  
  // Adiciona uma margem de erro que varia de acordo com o movimento da bola
  targetY += random(-errorMargin, errorMargin);

  // Movimento do computador com a mesma velocidade que o jogador
  if (computerY < targetY) {
    computerY += playerSpeed;  // Usa a mesma velocidade do jogador
  } else if (computerY > targetY) {
    computerY -= playerSpeed;  // Usa a mesma velocidade do jogador
  }

  // Limitar o movimento dentro da tela
  computerY = constrain(computerY, 0, height - computerHeight);
}
