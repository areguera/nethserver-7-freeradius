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

/**
 * Supplicants management for FreeRADIUS module
 *
 * @author Davide Principi <davide.principi@nethesis.it>
 * @since 1.0
 * @author Alain Reguera Delgado <alain.reguera@gmail.com>
 */
class Supplicants extends \Nethgui\Controller\TableController
{

    public $sortId = 30;

    public function initialize()
    {
        $columns = array(
            'key',
            'username',
            'password',
            'Description',
            'Actions'
        );

        $this
            ->setTableAdapter($this->getPlatform()->getTableAdapter('radiusd', 'supplicants'))
            ->setColumns($columns)
            ->addRowAction(new \NethServer\Module\FreeRADIUS\Supplicants\Modify('update'))
            ->addRowAction(new \NethServer\Module\FreeRADIUS\Supplicants\Modify('delete'))
            ->addTableAction(new \NethServer\Module\FreeRADIUS\Supplicants\Modify('create'))
            ->addTableAction(new \Nethgui\Controller\Table\Help('Help'))
	    ;

        parent::initialize();
    }

}
