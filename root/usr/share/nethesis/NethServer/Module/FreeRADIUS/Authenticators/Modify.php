<?php
namespace NethServer\Module\FreeRADIUS\Authenticators;

/*
 * Copyright (C) 2017 Nethesis S.r.l.
 *
 * This script is part of NethServer.
 *
 * NethServer is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * NethServer is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with NethServer.  If not, see <http://www.gnu.org/licenses/>.
 */

use Nethgui\System\PlatformInterface as Validate;
use Nethgui\Controller\Table\Modify as Table;

/**
 * Modify Authenticators
 *
 * Generic class to create/update/delete Authenticators records
 * 
 * @author Davide Principi <davide.principi@nethesis.it>
 * @since 1.0
 * @author Alain Reguera Delgado <alain.reguera@gmail.com>
 */
class Modify extends \Nethgui\Controller\Table\Modify
{
    public function initialize()
    {
        $parameterSchema = array(
            array('key', Validate::NOTEMPTY, Table::KEY),
            array('ipaddr', Validate::IP, Table::FIELD),
            array('secret', Validate::NOTEMPTY, Table::FIELD),
            array('Description', Validate::ANYTHING, Table::FIELD),
        );

        $this->setSchema($parameterSchema);

        parent::initialize();
    }

    public function prepareView(\Nethgui\View\ViewInterface $view)
    {
        parent::prepareView($view);
        $templates = array(
            'create' => 'NethServer\Template\FreeRADIUS\Authenticators\Modify',
            'update' => 'NethServer\Template\FreeRADIUS\Authenticators\Modify',
            'delete' => 'Nethgui\Template\Table\Delete',
        );
        $view->setTemplate($templates[$this->getIdentifier()]);
    }

    /**
     * Delete the record after the event has been successfully completed
     * @param string $key
     */
    protected function processDelete($key)
    {
        $accountDb = $this->getPlatform()->getDatabase('radiusd');
        $accountDb->setType($key, 'Authenticators-deleted');
        $deleteProcess = $this->getPlatform()->signalEvent('nethserver-freeradius-update', array($key));
        if ($deleteProcess->getExitCode() === 0) {
            parent::processDelete($key);
        }
    }

    protected function onParametersSaved($changedParameters)
    {
        if ($this->getIdentifier() === 'delete') {
            // delete case is handled in "processDelete()" method:
            // signalEvent() is invoked there.
            return;
        }
        $this->getPlatform()->signalEvent('nethserver-freeradius-update@post-process', array($this->parameters['key']));

    }

}
