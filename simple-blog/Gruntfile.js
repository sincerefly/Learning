module.exports = function(grunt) {
  // 项目配置信息.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    jshint: {
      options : {
        jshintrc: '.jshintrc',
        // eqeqeq: true,
        // tradiling: true,
        ignores: ['node_modules/**/*.js']
      },
      all: ['**/*.js']
    },
    coffee:{
      compile: {
        options: {
          sourceMap: false,
          bare: true
        },
        files: [{
          expand: true,
          cwd: "coffee/",
          src: '**/*.coffee',
          dest: 'js/',
          ext: '.js'
        }]
      }
    },
    watch: {
      coffee: {
        files: ['**/*.coffee'],
        tasks: ['coffee:compile']
      // },
      // js: {
      //   files: ['**/*.js'],
      //   tasks: ['jshint'],
      //   options: {
      //     livereload: true
      //   }
      }
    },
    nodemon: {
      dev: {
        script: 'bin/www',
        options: {
          args: [],
          ignoredFiles: [],
          watchedExtensions: ['js'],
          watchedFolders: ['./'],
          debug: true,
          delayTime: 1,
          env: {
            PORT: 3000
          },
          cwd: __dirname
        }
      }
    },
    concurrent: {
      tasks: ['watch','nodemon'],
      options: {
        logConcurrentOutput: true
      }
    }
  });
  // 加载"uglify"插件..
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-coffee');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-nodemon');
  grunt.loadNpmTasks('grunt-concurrent');
  //grunt.loadNpmTasks('grunt-ssh');

  grunt.option('force', true);

  // 注册默认任务.
  grunt.registerTask('default', ['concurrent']);
};
