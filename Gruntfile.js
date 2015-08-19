module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        jshint: {
            dev: {
                src: ['/static/stargazer/**/*.js']
            }
        },
        autoprefixer: {
            options: {
                // Task-specific options go here.
            },
            your_target: {
                src: 'static/stargazer/css/mainflex.css'
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
                command: ['cd /home/kuba/Pulpit/pycharm/bin',
                    'sudo sh pycharm.sh'].join('&&')
            }
        }
    });
    grunt.loadNpmTasks('grunt-autoprefixer');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-shell');
    grunt.registerTask('default', ['shell:pythonServer']);
    grunt.registerTask('pycharm', ['shell:pyCharm']);


}
