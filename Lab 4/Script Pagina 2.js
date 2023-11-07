// ==UserScript==
// @name         Script Pagina 2
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://silver-chere-54.tiiny.site/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=tiiny.site
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js#sha512-a+SUDuwNzXDvz4XrIcXHuCf089/iJAoN4lmrXJg18XnduKK6YlDHNRalv4yd1N40OKI80tFidF+rqTFKGPoWFQ==
// ==/UserScript==

(function() {
    'use strict';

    //Detectar la llave de cifrado buscando las letras mayusculas
    function detectarLetras() {
        const text = document.body.textContent;
        const letters = text.match(/[A-Z]/g);

        if (letters) {
            const concatenatedLetters = letters.join('');
            console.log('Llave de Cifrado:', concatenatedLetters);
            return concatenatedLetters

        } else {
            console.log('No se encontraron letras');
            return "Vacio"
        }


    }

    //almacenar clave
    const clave = detectarLetras();

    function desencriptar(clave) {
        const elementsWithClassM = document.querySelectorAll('[class*="M"]');
        const numberOfElements = elementsWithClassM.length;

        console.log(`Se encontraron ${numberOfElements} elementos cuya clase incluye 'M':`);

        const configure = {
              mode: CryptoJS.mode.ECB

         };

        elementsWithClassM.forEach(element => {



            const idCiphertext = element.id;

            const encryptionKey = CryptoJS.enc.Utf8.parse(clave); // Replace with your actual encryption key



            // Decrypt the ID
            const idDecrypted = CryptoJS.TripleDES.decrypt(idCiphertext, encryptionKey,configure);

            console.log(`ID: ${element.id}, Decrypted Text: ${idDecrypted.toString(CryptoJS.enc.Utf8)}`);
            const decryptedText = idDecrypted.toString(CryptoJS.enc.Utf8);
            const h2Element = document.createElement('h2');
            h2Element.textContent = decryptedText;
            document.body.appendChild(h2Element);
        });
    }

    // Execute the function when the page is loaded
    desencriptar(clave);
})();