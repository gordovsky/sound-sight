(function () {
    'use strict';

    angular
        .module('proj1', [
            'proj1.routes',
            'proj1.authentication'
        ])
        .run(run);

    angular
        .module('proj1.config', []);

    angular
        .module('proj1.routes', ['ngRoute']);

    //angular
    //    .module('proj1')
    //    .run(run);

    run.$inject = ['$http'];

    /**
     * @name run
     * @desc Update xsrf $http headers to align with Django's default
     */

    function run($http) {
        $http.default.xsrfHeaderName = 'X-CSRFToken';
        $http.default.xsrfCookieName = 'csrftoken';
    }
})();
