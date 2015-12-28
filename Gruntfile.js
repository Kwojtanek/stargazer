module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        concat: {
            options: {
                // define a string to put between each file in the concatenated output
                separator: ';'
            },
            dist: {
                // the files to concatenate
                src: [
                    'static/stargazer/simbad.min.js',
                    'static/stargazer/search.js',
                    'static/stargazer/angular/**/*.js',
                    'static/stargazer/angular/*.js'],
                // the location of the resulting JS file
                dest: 'static/stargazer/onefileangular.js'
            }
        },
        cssmin: {
            dist: {
                files: {
                    'static/stargazer/style.min.css': ['static/stargazer/css/*.css']
                }
            },
            files: ['static/stargazer/css/*.css'],
            tasks: ['cssmin']
        },
        uglify: {
            dist: {
                files: {
                    'static/stargazer/angul.min.js': ['static/stargazer/onefileangular.js']
                }
            }
        },
        watch: {
            css: {
                files: ['static/stargazer/css/*.css'],
                tasks: ['cssmin']
            },
            js: {
                files: ['static/stargazer/angular/*.js', 'static/stargazer/angular/**/*.js'],
                tasks: ['concat']
            }
        },
        shell: {
            pythonServer: {
                options: {
                    stdout: true
                },
                command: 'python manage.py runmodwsgi --reload-on-changes'
            },
            pyCharm: {
                options: {
                    stdout: true
                },
                command: ['cd /usr/local/pycharm-4.5.3/bin',
                    'sudo sh pycharm.sh'].join('&&')
            }
        }
    });
    grunt.loadNpmTasks('grunt-contrib-uglify');

    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-shell');
    grunt.registerTask('default', ['shell:pythonServer']);
    grunt.registerTask('w', ['watch']);
    grunt.registerTask('pycharm', ['shell:pyCharm']);


}
