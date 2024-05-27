
            var header = document.getElementById('header');
            var mobileMenu = document.getElementById('mobile-menu');
            var headerHeight = header.clientHeight;
    
            mobileMenu.onclick = function() {
                var isClosed = header.clientHeight === headerHeight;
                if(isClosed) {
                    header.style.height = 'auto';
                }
                else {
                    header.style.height = null;
                }
            }
    
    
            var menuItems = document.querySelectorAll('#nav li a[href*="#"]');
            for(var i = 0; i < menuItems.length; i++) {
                var menuItem = menuItems[i];
                
                menuItem.onclick = function(event) {
                    var isParentMenu = this.nextElementSibling && menuItem.nextElementSibling.classList.contains('subnav');
                    if(isParentMenu) {
                        event.preventDefault();
                    }
                    else {
                        header.style.height = null;
                    }
                }
            }