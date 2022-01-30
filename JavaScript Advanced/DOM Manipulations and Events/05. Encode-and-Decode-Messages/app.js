function encodeAndDecodeMessages() {
    let textInput = document.querySelector('textarea[placeholder*="Write"]');
    let decodeTextOutputField = document.querySelector('textarea[placeholder*="No"]');

    let buttonEncode = document.querySelectorAll('button')[0];
    let buttonDecode = document.querySelectorAll('button')[1];
    
    buttonEncode.addEventListener('click', onClickEncode);

    function onClickEncode(){
        let textForIterating = textInput.value;
        let textEncoded = "";

        for (letter of textForIterating){
            textEncoded += String.fromCharCode(letter.charCodeAt(0) + 1);
        }
        decodeTextOutputField.value = textEncoded;
        document.querySelector('textarea[placeholder*="Write"]').value = "";
    }

    buttonDecode.addEventListener('click', onClickDecode)

    function onClickDecode(){
        let textForIterating  =decodeTextOutputField.value;
        let textDecoded = "";
        for (letter of textForIterating){
            textDecoded += String.fromCharCode(letter.charCodeAt(0) - 1);
        }
        decodeTextOutputField.value = textDecoded;

    }

}