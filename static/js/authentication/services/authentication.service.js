//
///**
//* Authentication
//* @namespace proj1.authentication.services
//*/
//(function () {
//    'use strict';
//
//    angular
//        .module('proj1.authentification.services')
//        .factory('Authentification', Authentification);
//
//    Authentification.$inject = ['$cookies', '$http'];
//
//    /**
//    * @namespace Authentication
//    * @returns {Factory}
//    */
//
//
//    function Authentification($cookies, $http) {
//        /**
//        * @name Authentication
//        * @desc The Factory to be returned
//        */
//        var Authentification = {
//            register: register
//        };
//
//        return Authentification;
//
//        /**
//        * @name register
//        * @desc Try to register a new user
//        * @param {string} username The username entered by the user
//        * @param {string} password The password entered by the user
//        * @param {string} email The email entered by the user
//        * @returns {Promise}
//        * @memberOf proj1.authentication.services.authentication
//        */
//        function register(username, password, email) {
//            return $http.post('/api/v1/accounts/', {
//                username: username,
//                password: password,
//                email: email
//            });
//
//        }
//
//    }
//
//})();
