// Load Pyodide and execute the game code
languagePluginLoader.then(() => {
  pyodide.runPython(`
    import pygame

    pygame.init()

    // Get the canvas element
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');

    // Event listener for the start button
    const startButton = document.getElementById('startButton');
    startButton.addEventListener('click', startGame);

    // GLOBALS VARS
    const s_width = 450;
    const s_height = 700;
    const play_width = 300;  // meaning 300 // 10 = 30 width per block
    const play_height = 600;  // meaning 600 // 20 = 30 height per block
    const block_size = play_width / 10;

    const top_left_x = (s_width - play_width) / 2;
    const top_left_y = 50;

      // color
const gray = [119, 118, 110];
const white = [255, 255, 255];
const black = [0, 0, 0];
const red = [200, 0, 0];
const green = [0, 200, 0];
const blue = [0, 255, 255];
const bright_red = [255, 0, 0];
const bright_green = [0, 255, 0];
const sea_green = [0, 255, 255];
const orange = [255, 165, 0];
const yellow = [255, 255, 0];
const purple = [128, 0, 128];
const light_red = [255, 0, 0];

    const shape_colors = [
      (0, 255, 0),
      (255, 0, 0),
      (0, 255, 255),
      (255, 255, 0),
      (255, 165, 0),
      (0, 0, 255),
      (128, 0, 128)
    ];

    const shapes = [
      [['.....',
        '.....',
        '..00.',
        '.00..',
        '.....'],
       ['.....',
        '..0..',
        '..00.',
        '...0.',
        '.....']],

      [['.....',
        '.....',
        '.00..',
        '..00.',
        '.....'],
       ['.....',
        '..0..',
        '.00..',
        '.0...',
        '.....']],

      [['..0..',
        '..0..',
        '..0..',
        '..0..',
        '.....'],
       ['.....',
        '0000.',
        '.....',
        '.....',
        '.....']],

      [['.....',
        '.....',
        '.00..',
        '.00..',
        '.....']],

      [['.....',
        '.0...',
        '.000.',
        '.....',
        '.....'],
       ['.....',
        '..00.',
        '..0..',
        '..0..',
        '.....'],
       ['.....',
        '.....',
        '.000.',
        '...0.',
        '.....'],
       ['.....',
        '..0..',
        '..0..',
        '.00..',
        '.....']],

      [['.....',
        '...0.',
        '.000.',
        '.....',
        '.....'],
       ['.....',
        '..0..',
        '..0..',
        '..00.',
        '.....'],
       ['.....',
        '.....',
        '.000.',
        '.0...',
        '.....'],
       ['.....',
        '.00..',
        '..0..',
        '..0..',
        '.....']],

      [['.....',
        '..0..',
        '.000.',
        '.....',
        '.....'],
       ['.....',
        '..0..',
        '..00.',
        '..0..',
        '.....'],
       ['.....',
        '.....',
        '.000.',
        '..0..',
        '.....'],
       ['.....',
        '..0..',
        '.00..',
        '..0..',
        '.....']]
    ];

    // SHAPE FORMATS

    class Piece {
      constructor(x, y, shape) {
        this.x = x;
        this.y = y;
        this.shape = shape;
        this.color = shape_colors[shapes.indexOf(shape)];
        this.rotation = 0;
      }
    }

    function create_grid(locked_positions = {}) {
      const grid = Array.from(Array(20), () => Array(10).fill(black));

      for (const [key, color] of Object.entries(locked_positions)) {
        const [x, y] = key.split(',').map(Number);
        if (y >= 0) grid[y][x] = color;
      }

      return grid;
    }

    function convert_shape_format(shape) {
      const positions = [];
      const format = shape.shape[shape.rotation % shape.shape.length];

      for (let i = 0; i < format.length; i++) {
        const row = format[i];
        for (let j = 0; j < row.length; j++) {
          if (row[j] === '0') {
            positions.push([shape.x + j, shape.y + i]);
          }
        }
      }

      for (let i = 0; i < positions.length; i++) {
        const [x, y] = positions[i];
        positions[i] = [x - 2, y - 4];
      }

      return positions;
    }

    function valid_space(shape, grid) {
      const accepted_pos = shape.shape[shape.rotation % shape.shape.length].flatMap((row, i) =>
        row.split('').map((cell, j) => [shape.x + j, shape.y + i])
      );

      return accepted_pos.every(([x, y]) => y < 0 || (grid[y] && grid[y][x] === black));
    }

    function draw_grid(surface, row, col) {
      for (let i = 0; i < row; i++) {
        ctx.beginPath();
        ctx.moveTo(top_left_x, top_left_y + i * block_size);
        ctx.lineTo(top_left_x + play_width, top_left_y + i * block_size);
        ctx.strokeStyle = gray;
        ctx.stroke();
      }

      for (let j = 0; j < col; j++) {
        ctx.beginPath();
        ctx.moveTo(top_left_x + j * block_size, top_left_y);
        ctx.lineTo(top_left_x + j * block_size, top_left_y + play_height);
        ctx.strokeStyle = gray;
        ctx.stroke();
      }
    }

    function draw_window(surface, grid) {
      surface.fillStyle = black;
      surface.fillRect(0, 0, s_width, s_height);
      surface.font = '60px "Sofia", sans-serif';
      surface.fillStyle = white;
      surface.textAlign = 'center';
      surface.fillText('Tetris', top_left_x + play_width / 2, 30);

      for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
          surface.fillStyle = grid[i][j];
          surface.fillRect(top_left_x + j * block_size, top_left_y + i * block_size, block_size, block_size);
        }
      }

      surface.strokeStyle = red;
      surface.lineWidth = 4;
      surface.strokeRect(top_left_x, top_left_y, play_width, play_height);

      draw_grid(surface, 20, 10);
    }

    function main() {
      let locked_positions = {};
      let grid = create_grid(locked_positions);

      let change_piece = false;
      let run = true;
      let current_piece = new Piece(5, 0, shapes[Math.floor(Math.random() * shapes.length)]);
      let fall_time = 0;
      const fall_speed = 0.27;

      function update() {
        grid = create_grid(locked_positions);
        fall_time += 1;
        if (fall_time / 1000 >= fall_speed) {
          fall_time = 0;
          current_piece.y += 1;
          if (!valid_space(current_piece, grid) && current_piece.y > 0) {
            current_piece.y -= 1;
            change_piece = true;
          }
        }

        if (change_piece) {
          for (const [x, y] of convert_shape_format(current_piece)) {
            if (y >= 0) {
              grid[y][x] = current_piece.color;
            }
          }

          for (const [x, y] of convert_shape_format(current_piece)) {
            const key = `${x},${y}`;
            locked_positions[key] = current_piece.color;
          }

          current_piece = new Piece(5, 0, shapes[Math.floor(Math.random() * shapes.length)]);
          change_piece = false;
        }

        draw_window(ctx, grid);

        if (run) {
          requestAnimationFrame(update);
        }
      }

      update();
    }

    function startGame() {
      const warningMessage = document.getElementById('warningMessage');
      warningMessage.style.display = 'block';
      alert('Server started successfully!');
      main();
    }
  `);
});
