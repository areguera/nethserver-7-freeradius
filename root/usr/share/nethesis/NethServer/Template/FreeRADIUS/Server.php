<?php

/* @var $view Nethgui\Renderer\Xhtml */

echo $view->fieldset('Policy')->setAttribute('template', $T('Policy_label'))
    ->insert($view->checkBox('PolicyMAC', 'yes'))
    ->insert($view->checkBox('PolicyIEEE8021X', 'yes'));

echo $view->buttonList($view::BUTTON_SUBMIT | $view::BUTTON_HELP);
