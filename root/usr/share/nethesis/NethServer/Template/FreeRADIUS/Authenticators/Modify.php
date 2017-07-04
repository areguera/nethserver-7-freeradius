<?php

/* @var $view \Nethgui\Renderer\WidgetFactoryInterface */
$view->requireFlag($view::INSET_FORM);

if ($view->getModule()->getIdentifier() == 'update') {
    $headerText = $T('Update Authenticator `${0}`');
    $keyStyles = $view::STATE_READONLY;
} else {
    $headerText = $T('Create a new Authenticator');
    $keyStyles = 0;
}

echo $view->header('key')->setAttribute('template', $headerText);

echo $view->textInput('key', $keyStyles);
echo $view->textInput('ipaddr');
echo $view->textInput('secret');
echo $view->textInput('Description');

echo $view->buttonList($view::BUTTON_SUBMIT | $view::BUTTON_HELP | $view::BUTTON_CANCEL);
