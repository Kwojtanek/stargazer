module.exports = function(grunt) {
    grunt.initConfig({
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

    grunt.loadNpmTasks('grunt-shell');
    grunt.registerTask('default', ['shell:pythonServer']);
    grunt.registerTask('pycharm', ['shell:pyCharm']);


}
