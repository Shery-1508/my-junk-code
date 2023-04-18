const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const modelIndex = urlParams.get('model');
const galleryName = urlParams.get('gallery');

fetch('models.json')
    .then(response => response.json())
    .then(data => {
        const model = data.models[modelIndex];
        const gallery = model.galleries.find(g => g.name === galleryName);

        // Set the model name and gallery name in the page header
        document.querySelector('#model-name').textContent = model.name;
        document.querySelector('#gallery-name').textContent = gallery.name;

        // Create the lightbox container and elements
        const lightbox = document.createElement('div');
        lightbox.classList.add('lightbox');
        const lightboxContent = document.createElement('div');
        lightboxContent.classList.add('lightbox-content');
        const lightboxImage = document.createElement('img');
        lightboxImage.classList.add('lightbox-image');
        const lightboxPrev = document.createElement('button');
        lightboxPrev.classList.add('lightbox-prev');
        lightboxPrev.innerHTML = '&#10094;';
        const lightboxNext = document.createElement('button');
        lightboxNext.classList.add('lightbox-next');
        lightboxNext.innerHTML = '&#10095;';
        const lightboxClose = document.createElement('button');
        lightboxClose.classList.add('lightbox-close');
        lightboxClose.innerHTML = '&times;';

        // Add event listeners to the lightbox elements
        lightboxPrev.addEventListener('click', showPrevImage);
        lightboxNext.addEventListener('click', showNextImage);
        lightboxClose.addEventListener('click', closeLightbox);

        // Add the lightbox elements to the lightbox container
        lightboxContent.appendChild(lightboxImage);
        lightbox.appendChild(lightboxContent);
        lightbox.appendChild(lightboxPrev);
        lightbox.appendChild(lightboxNext);
        lightbox.appendChild(lightboxClose);
        document.body.appendChild(lightbox);

        // Add thumbnail images to the gallery page
        const galleryPics = document.querySelector('#gallery-pics');
        gallery.pics.forEach((pic, index) => {
            const img = document.createElement('img');
            img.src = pic.thumb;
            img.alt = 'Thumbnail image for ' + pic.src;
            img.addEventListener('click', () => {
                showImage(index);
            });
            galleryPics.appendChild(img);
        });

        // Show the initial image in the lightbox
        function showImage(index) {
            lightboxImage.src = gallery.pics[index].src;
            lightbox.style.display = 'block';
            currentImageIndex = index;
        }

        // Show the previous image in the lightbox
        function showPrevImage() {
            if (currentImageIndex > 0) {
                currentImageIndex--;
                lightboxImage.src = gallery.pics[currentImageIndex].src;
            }
        }

        // Show the next image in the lightbox
        function showNextImage() {
            if (currentImageIndex < gallery.pics.length - 1) {
                currentImageIndex++;
                lightboxImage.src = gallery.pics[currentImageIndex].src;
            }
        }

        // Close the lightbox
        function closeLightbox() {
            lightbox.style.display = 'none';
        }
    })
    .catch(error => console.error(error));
