<?php
namespace NethServer\Module\FreeRADIUS;

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

/**
 * Server management for FreeRADIUS module
 *
 * @author Davide Principi <davide.principi@nethesis.it>
 * @since 1.0
 * @author Alain Reguera Delgado <alain.reguera@gmail.com>
 */
class Server extends \Nethgui\Controller\AbstractController
{

    public $sortId = 10;

    public function initialize()
    {
        parent::initialize();

        $this
            ->declareParameter('PolicyMAC', Validate::BOOLEAN, array('configuration', 'radiusd', 'PolicyMAC'))
            ->declareParameter('PolicyIEEE8021X', Validate::BOOLEAN, array('configuration', 'radiusd', 'PolicyIEEE8021X'))
            ;
    }

    protected function onParametersSaved($changedParameters) {
        $this->getPlatform()->signalEvent('nethserver-freeradius-update@post-process');
    }

}
