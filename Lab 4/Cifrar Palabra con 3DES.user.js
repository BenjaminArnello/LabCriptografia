// ==UserScript==
// @name         Cifrar Palabra con 3DES
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Cifra una palabra con 3DES usando CryptoJS
// @author       You
// @match        https://cripto.tiiny.site/
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js
// ==/UserScript==

(function() {
    'use strict';

    // Palabra que quieres cifrar
    var palabra = "la";

    // Clave de cifrado 3DES (debe ser de 24 caracteres)
    var clave = "CRIPTOCRIPTOCRIPTOCRIPTO";

    // Convertir la clave a un formato adecuado
    var claveUtf8 = CryptoJS.enc.Utf8.parse(clave);

    // Cifrar la palabra utilizando 3DES en modo ECB
    var cifrado = CryptoJS.TripleDES.encrypt(palabra, claveUtf8, {
        mode: CryptoJS.mode.ECB
    });

    // Convertir el resultado cifrado a una representación legible en Base64
    var cifradoBase64 = cifrado.toString();

    console.log("Texto original: " + palabra);
    console.log("Texto cifrado: " + cifradoBase64);

    // Puedes realizar acciones adicionales con el resultado cifrado aquí, como enviarlo a un servidor o mostrarlo en la página web.
})();
