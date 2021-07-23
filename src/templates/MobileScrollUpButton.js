import React, { useEffect, useState } from 'react';

const MobileScrollUpButton = () => {
  const [hideButton, setHideButton] = useState(true);

  const [prevScrollHeight, setPrevScrollHeight] = useState(0);

  const showOrHide = () => {
    window.scrollY > prevScrollHeight ? setHideButton(true) : setHideButton(false);
    setPrevScrollHeight(window.scrollY);
  };

  useEffect(() => {
    window.addEventListener('scroll', showOrHide);
    //Make button disappear once scroll to top is complete
    window.onscroll = () => {
      if (window.scrollY === 0) {
        setHideButton(true);
        setPrevScrollHeight(0);
      }
    };
    return function cleanup() {
      window.removeEventListener('scroll', showOrHide);
    };
  });

  const handleClick = () => {
    window.scroll(0, 0);
  };

  return (
    <button className={`mobileScrollUpButton ${hideButton ? '' : 'fade'}`} onClick={handleClick}>
      Scroll to top
    </button>
  );
};

export default MobileScrollUpButton;
