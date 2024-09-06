
    // Function to show the modal by removing the 'hidden' class
    function show_modal(modalClass) {
        var modal = document.querySelector('.' + modalClass);
        if (modal) {
            modal.classList.remove('hidden');
        }
    }
    
    // Function to hide the modal by adding the 'hidden' class
    function hide_modal(modalClass) {
        var modal = document.querySelector('.' + modalClass);
        if (modal) {
            modal.classList.add('hidden');
        }
    }
    
    function close_parent_modal() {
        var modal = event.target.closest('.modal');
        if (modal) {
            modal.classList.add('hidden');
        }
    }

    function close_difficulty_modal(){
        if(difficulty == '-1'){
            //if user closes the modal without selecting difficulty, redirect beck to gamepicker
            window.location.href = gamePickerUrl;
        }
        else{
            close_parent_modal();
        }
    }

    function init_game(){
        if(typeof play_game == 'function'){
            play_game();
        }
    }

    function select_difficulty(){
        var difficultySelector = document.getElementById('difficultySelector');
        selected_difficulty = difficultySelector.value;
        send_difficulty(selected_difficulty);
    }

    function init_difficulty(){
        if(difficulty != '-1'){
            return init_game();
        }
        show_modal('difficulty-selector');
    }
 
 
    // In your JavaScript file
    function send_difficulty(selected_difficulty) {
        if (!(csrfToken && setDifficultyUrl)) {
            console.error('CSRF token is missing');
            return; // Exit if the CSRF token is not available
        }
        fetch(setDifficultyUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken  // Use the CSRF token variable
            },
            body: new URLSearchParams({
                'difficulty': selected_difficulty
            })
        })
        .then(response => {
            window.location.reload();
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }